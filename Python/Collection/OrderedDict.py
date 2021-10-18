# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import*
N = int(input())
d = OrderedDict()
for i in range(N):
    item = input().split()
    item_price = int(item[-1])
    item_name = " ".join(item[:-1])
    if(d.get(item_name)):
        d[item_name] += item_price
    else:
        d[item_name] = item_price
for i in d.keys():
    print(i, d[i])
