def solution():
    len_a, set_a = int(input()), set(input().split())
    len_b, set_b= int(input()), set(input().split())
    intersect = (set_a.intersection(set_b))
    return True if intersect == set_a else False

teks = ''
for _ in range(int(input())):
    teks += str(solution()) + '\n'
print(teks)