
---
title: 08丨利用assert语句来发现问题.
date: 2020-04-09 20:01:07
tags:
- python
- 编写高质量代码91个建议
categories:
- python
---

### 断言的正确用法.

断言只在需要确定.否则不能运行的地方,加入.印证确定代码无误.
并不是代码中实际编写的部分.
基本语法:

```
assert expression1 ["," expression2]
```

运行脚本加入 -O标志,忽略与断言相关的语句.



```python
x = 1
y = 2
# assert 如果不符合条件.抛出异常.
assert x == y, "not equals"
# 上下等价.
if __debug__ and not x == y:
    raise AssertionError("not equals")
```


```python
# 模板代码.如果input不是list.抛异常.
assert isinstance(input, list), 'input must be type of list'
```
