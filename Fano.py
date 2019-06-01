import math
import io
import sys
import numpy as np
import os
import copy

keys = dict()

def cut(l,n):
    part = l.sum() / n
    cutNum = 0
    if l.size == 2:
        return 1
    count = 1
    for i in range(1,l.size - 1):
        c = abs(l[0:i].sum() - part) < abs(l[i:l.size + 1].sum() - part)
        if c < count:
            count = c
            cutNum = i

    return cutNum


def coding(l,n,s):
    if l.size == 1:
        if(l[0] not in keys.keys()):
            keys[l[0]] = s
        return
    else:

        cutNum = cut(l,n)
        coding(l[0:cutNum],n,s + str(0))
        coding(l[cutNum:l.size],n,s + str(1))



if __name__ == "__main__":

    s = input('[*] 请输入字符概率分布:')
    n = int(input('[*] 请输入编码进制：'))

    arr = s.split(" ")
    l = np.array(arr).astype(np.float)
    # if l.sum() != 1:
    #     print('[*] 求和不为1')
    #     os._exit()
    l = l[np.argsort(-l)]
    print('[*] 排序后的概率分布：',l)
    coding(l,n,'')
    print('[*] 费诺编码结果:',keys)


