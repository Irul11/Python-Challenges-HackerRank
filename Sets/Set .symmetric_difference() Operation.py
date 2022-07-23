# 06-11-2022

# n = int(input())
# student_n = input().split()

# b = int(input())
# student_b = input().split()
student_n = [2,4,3,5,7,1]
student_b = (3,4,5,9,8,11)
sets = set(student_n)

sym_diff = sets.symmetric_difference(student_b)
print((sym_diff))