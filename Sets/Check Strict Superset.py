a = input().split()
a = sorted(set(a))
n = int(input())
result = True
for i in range(n):
    for j in (input().split()):
        if j not in a:
            result = False
print(result)