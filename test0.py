import csv
import networkx as nx
import matplotlib.pyplot as plt
import itertools as itr

tuple_list_0 = [(2, 0), (2, 1), (2, 3), (2, 4)]
tuple_list_1 = [(3, 1), (3, 2), (3, 4)]
tuple_list_2 = [(4, 2), (4, 3), (4, 5)]

print(type(tuple_list_0))       # <class 'list'>
print(type(tuple_list_0[0]))    # <class 'tuple'>

list_0_0 = list(tuple_list_0[0])
print(list_0_0)                 # [2, 0]
print(type(list_0_0))           # <class 'list'>

list_0, list_1, list_2 = [], [], []
for x in tuple_list_0:
    y = list(x)
    list_0.append(y)

for x in tuple_list_1:
    xx = list(x)
    list_1.append(xx)

for x in tuple_list_2:
    xx = list(x)
    list_2.append(xx)

print(list_0)                   # [[2, 0], [2, 1], [2, 3], [2, 4]]
print(list_1)                   # [[3, 1], [3, 2], [3, 4]]
print(list_2)                   # [[4, 2], [4, 3], [4, 5]]

# 入れ替え
for x in list_1:
    print(x)

'''
    list_1[0][0], list_1[0][1] = list_1[0][1], list_1[0][0]
print(list_1)

if list_1[0] in list_0:
    print("match")
else:
    print("unmatch")
'''