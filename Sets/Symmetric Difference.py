if __name__ == '__main__':
    n = int(input())
    student_n = set(map(int, input().split()))
    m = int(input())
    student_m = set(map(int, input().split()))
    sym_diff = student_n.symmetric_difference(student_m)

    for i in sorted(sym_diff):
        print(i)
