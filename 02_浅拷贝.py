#!/usr/bin/env python
# -*- coding:utf-8 -*-
# mr wang

import copy
"""
深拷贝与浅拷贝是对内存数据的数据，目的的能够单独操作数据
1.引入copy模块
2.copy.copy（objeck）
    object：要拷贝的对象
    小结：浅拷贝只拷贝对象的第一层（顶层）数据
"""
a = [11, 22]
b = [33, 44]
c = [a, b]
d = copy.copy(c)
print("a-------->%d    c[0]------>%d " % (id(a), id(c[0])))
print("c-------->%d     d--------->%d" % (id(c), id(d)))
print("a------->%d      d[0]---------->%d" % (id(a), id(d[0])))
c.append(1)
d.append(2)
print(c, d)
