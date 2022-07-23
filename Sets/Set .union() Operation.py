# 06-11-2022

n = int(input())
student_n = input().split()
b = int(input())
student_b = input().split()
sets = set(student_n)
union = sets.union(student_b)
print(len(union))