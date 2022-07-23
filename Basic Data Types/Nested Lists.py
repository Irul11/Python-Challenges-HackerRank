lis = []
score_list = []
# Function to get the second element for each nested list
def sec_nest(n):
    return n[-1]

def second(n):
    x = min(n)
    while x in n:
        n.remove(x)
    return min(n)

def minimum(lis, n):
    lowest = list(filter(lambda x: x[-1] == n, lis))
    lowest = sorted(lowest)
    return lowest

for _ in range(int(input())):
    name = input()
    score = float(input())
    lis += [[name, score]]
    score_list += [score]
lis = sorted(lis, key=sec_nest)

lowest = minimum(lis, second(score_list))
for s in lowest:
    print(s[0])
