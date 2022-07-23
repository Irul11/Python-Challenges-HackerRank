# 06-11-2022

len_sets = int(input())
sets = set(map(int, input().split()))

for _ in range(int(input())):
    a, b = input().split()
    sets2 = set(map(int, input().split()))
    (getattr(sets, a)(sets2))
print(sum(sets))