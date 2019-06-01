import math
import io
import sys
import numpy as np
import os
import copy


keys = dict()


class Node:
    son = []
    num = 0
    key = ''
    def __init__(self,i):
        self.num = i
        self.son = []

    def getNumber(self):
        return self.num

    def getSon(self):
        return self.son


def buildTree(l,n):
    ll = []
    for i in range(l.size):
        ll.append(Node(l[i]))
    d = 0
    if l.size % (n -  1) != 1 & n != 2:
        d = n - l.size % (n - 1)

    for i in range(d):
        ll.append(Node(0))



    while len(ll) > 1:
        t = Node(0)
        for i in range(n):
            ll[len(ll) - n + i].key = str(i)
            t.num = t.num + ll[len(ll) - n + i].num
            t.son.append(ll[len(ll) - n + i])
        for i in range(n):
            ll.pop()

        ll.append(t)
        for i in range(len(ll)):
            for j in range(i,len(ll)):
                if ll[i].num < ll[j].num:
                    cache = copy.deepcopy(ll[i])
                    ll[i] = ll[j]
                    ll[j] = cache
    return ll[0]

def findTree(current,before):
    if len(current.son) == 0:
        keys[str(current.num)] = before + current.key
        return
    for i in current.son:
        before = before + i.key
        findTree(i,before)





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
    tree = buildTree(l,n)
    findTree(tree,'')
    print('[*] 哈夫曼编码结果:',keys)


