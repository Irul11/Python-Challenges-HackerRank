def average(array):
    # your code goes here
    sets = set(array)
    return round(sum(sets)/len(sets), 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)