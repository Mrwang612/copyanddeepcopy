a = [11, 22]
b = [33, 44]
c = [a, b]
print("------列表切片------")
d = c[:]
print("c------->%d  d------->%d" % (id(c), id(d)))
print("a-------->%d   d[0]----->%d" % (id(a), id(d[0])))


print("--------字典-------")
c = {"key1": a, "key2": b}
d = c.copy()
print('a--->%d     c["key1"]--->%d'%(id(a),id(c["key1"])))
print('c--->%d     d--->%d'%(id(c),id(d)))
print('a--->%d     d["key1"]--->%d'%(id(a),id(d["key1"])))
