# -*- coding: utf-8 -*-

#    File Name：       yake
#    Description :
#    Author :          LvYang
#    date：            2019/4/12
#    Change Activity:  2019/4/12:

class Yake(object):

    def __init__(self):
        self.money = 1000

    def buy(self, price):
        if self.money>price:
            return "success"
        else:
            return "No money"