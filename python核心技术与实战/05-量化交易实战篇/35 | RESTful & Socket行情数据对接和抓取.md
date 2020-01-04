
---
title: 35 | RESTful & Socket行情数据对接和抓取
date: 2020-01-04 20:10:07
tags:
- python
- 极客时间
categories:
- python核心技术与实战
---

### 行情数据
回顾上一节我们提到的，交易所是一个买方、卖方之间的公开撮合平台。买卖方把需要 / 可提供的商品数量和愿意出 / 接受的价格提交给交易所，交易所按照公平原则进行撮合交易。

那么撮合交易是怎么进行的呢？假设你是一个人肉比特币交易所，大量的交易订单往你这里汇总，你应该如何选择才能让交易公平呢？

显然，最直观的操作就是，把买卖订单分成两个表，按照价格由高到低排列。下面的图，就是买入和卖出的委托表。

如果最高的买入价格小于最低的卖出价格，那就不会有任何交易发生。这通常是你看到的委托列表的常态。

如果最高的买入价格和最低的卖出价格相同，那么就尝试进行撮合。比如 BTC 在 9002.01 就会发生撮合，最后按照 9002.01 的价格，成交 0.0330 个 BTC。当然，交易完成后，小林未完成部分的订单（余下 0.1126 - 0.0330 = 0.0796 个 BTC 未卖出），还会继续在委托表里。

不过你可能会想，如果买入和卖出的价格有交叉，那么成交价格又是什么呢？事实上，这种情况并不会发生。我们来试想一下下面这样的场景。

如果你尝试给一个委托列表里加入一个新买入订单，它的价格比所有已有的最高买入价格高，也比所有的卖出价格高。那么此时，它会直接从最低的卖出价格撮合。等到最低价格的卖出订单吃完了，它便开始吃价格第二低的卖出订单，直到这个买入订单完全成交。反之亦然。所以，委托列表价格不会出现交叉。

当然，请注意，这里我说的只是限价订单的交易方式。而对于市价订单，交易规则会有一些轻微的区别，这里我就不详细解释了，主要是让你有个概念。

其实说到这里，所谓的“交易所行情”概念就呼之欲出了。交易所主要有两种行情数据：委托账本（Order Book）和活动行情（Tick data）。

我们把委托表里的具体用户隐去，相同价格的订单合并，就得到了下面这种委托账本。我们主要观察右边的数字部分，其中：

* 上半部分里，第一列红色数字代表 BTC 的卖出价格，中间一列数字是这个价格区间的订单 BTC 总量，最右边一栏是从最低卖出价格到当前价格区间的积累订单量。
* 中间的大字部分，9994.10 USD 是当前的市场价格，也就是上一次成交交易的价格。
* 下面绿色部分的含义与上半部分类似，不过指的是买入委托和对应的数量。

这张图中，最低的卖出价格比最高的买入价格要高 6.51 USD，这个价差通常被称为 Spread。这里验证了我们前面提到的，委托账本的价格永不交叉； 同时，Spread 很小也能说明这是一个非常活跃的交易所。

每一次撮合发生，意味着一笔交易（Trade）的发生。卖方买方都很开心，于是交易所也很开心地通知行情数据的订阅者：刚才发生了一笔交易，交易的价格是多少，成交数量是多少。这个数据就是活动行情 Tick。

有了这些数据，我们也就掌握了这个交易所的当前状态，可以开始搞事情了。

### Websocket 介绍
在本文的开头我们提到过：行情数据很讲究时效性。所以，行情从交易所产生到传播给我们的程序之间的延迟，应该越低越好。通常，交易所也提供了 REST 的行情数据抓取接口。比如下面这段代码：


```python
import requests
import timeit
 
 
def get_orderbook():
  orderbook = requests.get("https://api.gemini.com/v1/book/btcusd").json()
 
 
n = 10
latency = timeit.timeit('get_orderbook()', setup='from __main__ import get_orderbook', number=n) * 1.0 / n
print('Latency is {} ms'.format(latency * 1000))
```

    Latency is 1216.6739538000002 ms


我在美国纽约附近城市的一个服务器上测试了这段代码，你可以看到，平均每次访问 orderbook 的延迟有 0.25 秒左右。显然，如果在国内，这个延迟只会更大。按理说，这两个美国城市的距离很短，为什么延迟会这么大呢？

这是因为，REST 接口本质上是一个 HTTP 接口，在这之下是 TCP/TSL 套接字（Socket）连接。每一次 REST 请求，通常都会重新建立一次 TCP/TSL 握手；然后，在请求结束之后，断开这个链接。这个过程，比我们想象的要慢很多。

举个例子来验证这一点，在同一个城市我们试验一下。我从纽约附近的服务器和 Gemini 在纽约的服务器进行连接，TCP/SSL 握手花了多少时间呢？


```python
curl -w "TCP handshake: %{time_connect}s, SSL handshake: %{time_appconnect}s\n" -so /dev/null https://www.gemini.com
```


      File "<ipython-input-2-946ae0cd5ce7>", line 1
        curl -w "TCP handshake: %{time_connect}s, SSL handshake: %{time_appconnect}s\n" -so /dev/null https://www.gemini.com
                                                                                      ^
    SyntaxError: invalid syntax



结果显示，HTTP 连接构建的过程，就占了一大半时间！也就是说，我们每次用 REST 请求，都要浪费一大半的时间在和服务器建立连接上，这显然是非常低效的。很自然的你会想到，我们能否实现一次连接、多次通信呢？

事实上，Python 的某些 HTTP 请求库，也可以支持重用底层的 TCP/SSL 连接。但那种方法，一来比较复杂，二来也需要服务器的支持。该怎么办呢？其实，在有 WebSocket 的情况下，我们完全不需要舍近求远。

我先来介绍一下 WebSocket。WebSocket 是一种在单个 TCP/TSL 连接上，进行全双工、双向通信的协议。WebSocket 可以让客户端与服务器之间的数据交换变得更加简单高效，服务端也可以主动向客户端推送数据。在 WebSocket API 中，浏览器和服务器只需要完成一次握手，两者之间就可以直接创建持久性的连接，并进行双向数据传输。

概念听着很痛快，不过还是有些抽象。为了让你快速理解刚刚的这段话，我们还是来看两个简单的例子。二话不说，先看一段代码：


```python
import websocket
import thread
 
# 在接收到服务器发送消息时调用
def on_message(ws, message):
    print('Received: ' + message)
 
# 在和服务器建立完成连接时调用   
def on_open(ws):
    # 线程运行函数
    def gao():
        # 往服务器依次发送 0-4，每次发送完休息 0.1 秒
        for i in range(5):
            time.sleep(0.01)
            msg="{0}".format(i)
            ws.send(msg)
            print('Sent: ' + msg)
        # 休息 1 秒用于接受服务器回复的消息
        time.sleep(1)
        
        # 关闭 Websocket 的连接
        ws.close()
        print("Websocket closed")
    
    # 在另一个线程运行 gao() 函数
    thread.start_new_thread(gao, ())
 
 
if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://echo.websocket.org/",
                              on_message = on_message,
                              on_open = on_open)
    
    ws.run_forever()
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-1-f88baa1bc71c> in <module>
          1 import websocket
    ----> 2 import thread
          3 
          4 # 在接收到服务器发送消息时调用
          5 def on_message(ws, message):


    ModuleNotFoundError: No module named 'thread'


这段代码尝试和wss://echo.websocket.org建立连接。当连接建立的时候，就会启动一条线程，连续向服务器发送 5 条消息。

通过输出可以看出，我们在连续发送的同时，也在不断地接受消息。这并没有像 REST 一样，每发送一个请求，要等待服务器完成请求、完全回复之后，再进行下一个请求。换句话说，我们在请求的同时也在接受消息，这也就是前面所说的”全双工“。

再来看第二段代码。为了解释”双向“，我们来看看获取 Gemini 的委托账单的例子。


```python
import ssl
import websocket
import json
 
# 全局计数器
count = 5
 
def on_message(ws, message):
    global count
    print(message)
    count -= 1
    # 接收了 5 次消息之后关闭 websocket 连接
    if count == 0:
        ws.close()
 
if __name__ == "__main__":
    ws = websocket.WebSocketApp(
        "wss://api.gemini.com/v1/marketdata/btcusd?top_of_book=true&offers=true",
        on_message=on_message)
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-4-00b6ecb101b9> in <module>
         15 
         16 if __name__ == "__main__":
    ---> 17     ws = websocket.WebSocketApp(
         18         "wss://api.gemini.com/v1/marketdata/btcusd?top_of_book=true&offers=true",
         19         on_message=on_message)


    AttributeError: module 'websocket' has no attribute 'WebSocketApp'


可以看到，在和 Gemini 建立连接后，我们并没有向服务器发送任何消息，没有任何请求，但是服务器却源源不断地向我们推送数据。这可比 REST 接口“每请求一次获得一次回复”的沟通方式高效多了！

因此，相对于 REST 来说，Websocket 是一种更加实时、高效的数据交换方式。当然缺点也很明显：因为请求和回复是异步的，这让我们程序的状态控制逻辑更加复杂。这一点，后面的内容里我们会有更深刻的体会。

### 行情抓取模块
有了 Websocket 的基本概念，我们就掌握了和交易所连接的第二种方式。

事实上，Gemini 提供了两种 Websocket 接口，一种是 Public 接口，一种为 Private 接口。

Public 接口，即公开接口，提供 orderbook 服务，即每个人都能看到的当前挂单价和深度，也就是我们这节课刚刚详细讲过的 orderbook。

而 Private 接口，和我们上节课讲的挂单操作有关，订单被完全执行、被部分执行等等其他变动，你都会得到通知。

我们以 orderbook 爬虫为例，先来看下如何抓取 orderbook 信息。下面的代码详细写了一个典型的爬虫，同时使用了类进行封装，希望你不要忘记我们这们课的目的，了解 Python 是如何应用于工程实践中的：


```python
import copy
import json
import ssl
import time
import websocket
 
 
class OrderBook(object):
 
    BIDS = 'bid'
    ASKS = 'ask'
 
    def __init__(self, limit=20):
 
        self.limit = limit
 
        # (price, amount)
        self.bids = {}
        self.asks = {}
 
        self.bids_sorted = []
        self.asks_sorted = []
 
    def insert(self, price, amount, direction):
        if direction == self.BIDS:
            if amount == 0:
                if price in self.bids:
                    del self.bids[price]
            else:
                self.bids[price] = amount
        elif direction == self.ASKS:
            if amount == 0:
                if price in self.asks:
                    del self.asks[price]
            else:
                self.asks[price] = amount
        else:
            print('WARNING: unknown direction {}'.format(direction))
 
    def sort_and_truncate(self):
        # sort
        self.bids_sorted = sorted([(price, amount) for price, amount in self.bids.items()], reverse=True)
        self.asks_sorted = sorted([(price, amount) for price, amount in self.asks.items()])
 
        # truncate
        self.bids_sorted = self.bids_sorted[:self.limit]
        self.asks_sorted = self.asks_sorted[:self.limit]
 
        # copy back to bids and asks
        self.bids = dict(self.bids_sorted)
        self.asks = dict(self.asks_sorted)
 
    def get_copy_of_bids_and_asks(self):
        return copy.deepcopy(self.bids_sorted), copy.deepcopy(self.asks_sorted)
 
 
class Crawler:
    def __init__(self, symbol, output_file):
        self.orderbook = OrderBook(limit=10)
        self.output_file = output_file
 
        self.ws = websocket.WebSocketApp('wss://api.gemini.com/v1/marketdata/{}'.format(symbol),
                                         on_message = lambda ws, message: self.on_message(message))
        self.ws.run_forever(sslopt={'cert_reqs': ssl.CERT_NONE})
 
    def on_message(self, message):
        # 对收到的信息进行处理，然后送给 orderbook
        data = json.loads(message)
        for event in data['events']:
            price, amount, direction = float(event['price']), float(event['remaining']), event['side']
            self.orderbook.insert(price, amount, direction)
 
        # 整理 orderbook，排序，只选取我们需要的前几个
        self.orderbook.sort_and_truncate()
 
        # 输出到文件
        with open(self.output_file, 'a+') as f:
            bids, asks = self.orderbook.get_copy_of_bids_and_asks()
            output = {
                'bids': bids,
                'asks': asks,
                'ts': int(time.time() * 1000)
            }
            f.write(json.dumps(output) + '\n')
 
 
if __name__ == '__main__':
    crawler = Crawler(symbol='BTCUSD', output_file='BTCUSD.txt')
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-1-cec014539940> in <module>
         86 
         87 if __name__ == '__main__':
    ---> 88     crawler = Crawler(symbol='BTCUSD', output_file='BTCUSD.txt')
    

    <ipython-input-1-cec014539940> in __init__(self, symbol, output_file)
         60         self.output_file = output_file
         61 
    ---> 62         self.ws = websocket.WebSocketApp('wss://api.gemini.com/v1/marketdata/{}'.format(symbol),
         63                                          on_message = lambda ws, message: self.on_message(message))
         64         self.ws.run_forever(sslopt={'cert_reqs': ssl.CERT_NONE})


    AttributeError: module 'websocket' has no attribute 'WebSocketApp'


代码比较长，接下来我们具体解释一下。

这段代码的最开始，封装了一个叫做 orderbook 的 class，专门用来存放与之相关的数据结构。其中的 bids 和 asks 两个字典，用来存储当前时刻下的买方挂单和卖方挂单。

此外，我们还专门维护了一个排过序的 bids_sorted 和 asks_sorted。构造函数有一个参数 limit，用来指示 orderbook 的 bids 和 asks 保留多少条数据。对于很多策略，top 5 的数据往往足够，这里我们选择的是前 10 个。

再往下看，insert() 函数用于向 orderbook 插入一条数据。需要注意，这里的逻辑是，如果某个 price 对应的 amount 是 0，那么意味着这一条数据已经不存在了，删除即可。insert 的数据可能是乱序的，因此在需要的时候，我们要对 bids 和 asks 进行排序，然后选取前面指定数量的数据。这其实就是 sort_and_truncate() 函数的作用，调用它来对 bids 和 asks 排序后截取，最后保存回 bids 和 asks。

接下来的 get_copy_of_bids_and_asks() 函数，用来返回排过序的 bids 和 asks 数组。这里使用深拷贝，是因为如果直接返回，将会返回 bids_sorted 和 asks_sorted 的指针；那么，在下一次调用 sort_and_truncate() 函数的时候，两个数组的内容将会被改变，这就造成了潜在的 bug。

最后来看一下 Crawler 类。构造函数声明 orderbook，然后定义 Websocket 用来接收交易所数据。这里需要注意的一点是，回调函数 on_message() 是一个类成员函数。因此，应该你注意到了，它的第一个参数是 self，这里如果直接写成 on_message = self.on_message 将会出错。

为了避免这个问题，我们需要将函数再次包装一下。这里我使用了前面学过的匿名函数，来传递中间状态，注意我们只需要 message，因此传入 message 即可。

剩下的部分就很清晰了，on_message 回调函数在收到一个新的 tick 时，先将信息解码，枚举收到的所有改变；然后插入 orderbook，排序；最后连同 timestamp 一并输出即可。

虽然这段代码看起来挺长，但是经过我这么一分解，是不是发现都是学过的知识点呢？这也是我一再强调基础的原因，如果对你来说哪部分内容变得陌生了（比如面向对象编程的知识点），一定要记得及时往前复习，这样你学起新的更复杂的东西，才能轻松很多。

回到正题。刚刚的代码，主要是为了抓取 orderbook 的信息。事实上，Gemini 交易所在建立数据流 Websocket 的时候，第一条信息往往非常大，因为里面包含了那个时刻所有的 orderbook 信息。这就叫做初始数据。之后的消息，都是基于初始数据进行修改的，直接处理即可。

### 总结
这节课我们继承上一节，从委托账本讲起，然后讲述了 WebSocket 的定义、工作机制和使用方法，最后以一个例子收尾，带你学会如何爬取 Orderbook 的信息。希望你在学习这节课的内容时，能够和上节课的内容联系起来，仔细思考 Websocket 和 RESTFul 的区别，并试着总结网络编程中不同模型的适用范围。
