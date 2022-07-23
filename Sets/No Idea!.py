_, _ = input().split()
array = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

result = 0
for i in array:
    if i in set_a:
        result += 1
    elif i in set_b:
        result -= 1

print(result)
# print(len(array.intersection(set_a)) - len(array.intersection(set_b)))
