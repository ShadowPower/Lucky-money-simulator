#! python3
#coding: utf-8

import math, random
class RedPacket:
    __remainSize = 0
    __remainMoney = 0

    def __init__(self, size, money):
        self.__remainSize = int(size)
        self.__remainMoney = int(money * 100)

    def is_empty(self):
        return self.__remainSize <= 0

    def get_money(self):
        if self.is_empty():
            return 0

        if self.__remainSize == 1:
            self.__remainSize = 0
            return self.__remainMoney / 100

        money = random.random() * (self.__remainMoney / self.__remainSize * 2)
        money = int(money) if money >= 1 else 1
        self.__remainSize -= 1
        self.__remainMoney -= money
        return money / 100
