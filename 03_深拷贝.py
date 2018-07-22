#!/usr/bin/env python
# -*- coding:utf-8 -*-
# mr wang


""" 深拷贝与浅拷贝是对内存数据的复制，目的是能够单独操作数据
深拷贝：
  1. 引入copy模块
  2. copy.deepcopy(object)
     object: 要拷贝的对象
 小结： 深拷贝是要拷贝对象的所有层的拷贝

"""
import copy
a = [11, 22]
b = (1, [33, 44])
c = [a, b]

d = copy.deepcopy(c)

d.append(1)

print('a--->%d     c[0]--->%d' % (id(a),id(c[1])))
print('c--->%d     d--->%d' % (id(c),id(d)))
print('a--->%d     d[0]--->%d' % (id(a),id(d[0])))
print(c)
print(d)