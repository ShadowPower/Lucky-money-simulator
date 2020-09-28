#! python3
#coding:utf-8
from decimal import *
from functools import reduce as 合并
import random as 随机

输入 = input
打印 = print
暂停 = input
字符串 = str
整数 = int
浮点数 = float
洗牌 = 随机.shuffle
长度 = len
范围 = range
遍历索引和元素 = enumerate
随机生成一个实数 = 随机.uniform
上界 = ROUND_UP
下界 = ROUND_DOWN

class 小数(Decimal):
    def 量化(self, 范围: Decimal, rounding=None):
        return self.quantize(范围, rounding)
