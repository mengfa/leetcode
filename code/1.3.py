# -*- coding: utf-8 -*-

#    File Name：       1.3
#    Description :
#    Author :          LvYang
#    date：            2019/8/19
#    Change Activity:  2019/8/19:

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
        print(previous_lines)

# Example use on a file

a = [['abc','abc1 ','abc2 ','abcc ','abc1c ','abc22 ','python','abc' ],['abc','abc1','abc2','abc' ],['abc','abc1','abc2','python','abc' ],['abc','abc1','abc2','abc' ]]



if __name__ == '__main__':
    for f in a:
        for line, prevlines in search(f, 'python', 3):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)




    # with open(r'../../cookbook/somefile.txt') as f:
    #     for line, prevlines in search(f, 'python', 5):
    #         for pline in prevlines:
    #             print(pline, end='')
    #         print(line, end='')
    #         print('-' * 20)