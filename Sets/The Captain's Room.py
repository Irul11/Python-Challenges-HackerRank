# 06-12-2022
from collections import Counter
_, arr = int(input()), input().split()
a, b = set(), set()
for i in arr:
    a.add(i) if i not in a else b.add(i)
print(a.difference(b).pop())

