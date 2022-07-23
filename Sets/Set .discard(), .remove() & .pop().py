# 06-11-2022

# len_s = int(input())
s = set(map(int, input().strip().split()))

# def erase(sets, method, element):
#     if method == 'pop':
#         sets.pop()
#     elif method == 'remove':
#         sets.remove(element)
#     elif method == 'discard':
#         sets.discard(element)
# print(s)
for _ in range(int(input())):
    a = input().split()
    # print(s)
    method = a[0]
    element = None
    if len(a) == 2:
        element = int(a[1])
    if method == 'pop':
        getattr(s, method)()
    else:
        getattr(s, method)(int(a[1]))

print(s)