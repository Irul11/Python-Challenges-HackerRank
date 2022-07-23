n = int(input())
arr = map(int, input().split())
arr = list(arr)
winner = max(arr)
while winner in arr:
    arr.remove(winner)
print(max(arr))