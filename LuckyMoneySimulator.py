#! python3
#coding:utf-8
from decimal import *
from functools import reduce
import random

#作者非常懒
D = Decimal

def 随机分配(红包列表, 红包个数):
    for i, 当前红包金额 in enumerate(红包列表):
        随机增减金额 = D(random.uniform(0, float(当前红包金额 - D('0.01')))).quantize(D('.00'))
        当前红包金额 -= 随机增减金额
        红包列表[i] = 当前红包金额 #将结果写回去
        红包列表[int(random.uniform(0, 红包个数))] += 随机增减金额
    random.shuffle(红包列表)

总金额 = D(input('请输入总金额：')).quantize(D('.00'))
红包个数 = int(input('请输入红包数目：'))

#平均分配后，较大的那批红包的个数
大红包数 = int(总金额 * 100) % 红包个数

较大的那批红包金额 = (总金额 / D(红包个数)).quantize(D('.00'), ROUND_UP)
较小的那批红包金额 = (总金额 / D(红包个数)).quantize(D('.00'), ROUND_DOWN)

#生成初始红包状态
普通红包 = []
for 当前编号 in range(红包个数):
    if 当前编号 < 大红包数:
        普通红包.append(较大的那批红包金额)
    else:
        普通红包.append(较小的那批红包金额)

拼手气红包 = 普通红包[:]
随机分配(拼手气红包, 红包个数)

#输出分配结果
for i, 当前红包 in enumerate(拼手气红包):
    print('第', i+1, '个红包：', str(当前红包));

#实现Decimal求和
def add(x, y):
    return x + y
print('最终红包总金额：', reduce(add, 拼手气红包))

#暂停查看结果
input()
