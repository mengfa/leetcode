# -*- coding: utf-8 -*-

#    File Name：       1
#    Description :
#    Author :          LvYang
#    date：            2019/3/19
#    Change Activity:  2019/3/19:

# 执行用时为 24 ms 的范例
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        
        用于的符号

        a[::-1]
        表示对于给定的字符串 / 列表 / 元组，您可以使用该格式对所述对象进行切片

        < object_name > [ < start_index >, < stop_index >, < step >]
        这意味着该对象将从给定的起始索引切换每个“步”索引，直到停止索引（不包括停止索引）并将其返回给您。

        如果缺少起始索引或停止索引，它将占用默认值作为给定字符串 / 列表 / 元组的起始索引和停止索引。如果该步骤留空，则它采用默认值1，即它通过每个索引。

        所以，

        a = '1234'
        print
        a[::2]
        会打印

        13
        现在索引在这里也是步数，支持负数。因此，如果给出 - 1
        索引，则转换为len（a）-1
        索引。如果你给 - x作为步数，那么它将从起始索引开始每个第x个值，直到反向的停止索引。例如

        a = '1234'
        print
        a[3:0:-1]
        这会回来

        432
        注意，它不返回4321因为，不包括停止索引。

        现在在你的情况下，

        str(int(a[::-1]))
        只会反转存储在字符串中的给定整数，然后将其转换回字符串

        即“1234” - >“4321” - > 4321 - >“4321”

        如果你要做的只是反转给定的字符串，那么只需一个[:: - 1]
        即可。
        '''
        result = s[::-1]
        return result