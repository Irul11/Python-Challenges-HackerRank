def print_rangoli(size):
    # your code goes here
    lis = ['']*(n*2-1)
    a,b = n, n
    ###
    for i in range (ord('a'), ord('a')+n):
        lis[a-1], lis[b-1] = chr(i), chr(i)
        a, b = a-1, b+1
    lis = [lis]*(n*2-1)

    ###
    c, d = n, n
    e = lis[0]
    for j in range(int((len(lis)+1)/2), 0, -1):
        x = ['-']*(n-j) + lis[c-1][:j] + list(reversed(lis[c-1][:j-1])) + ['-']*(n-j)
        lis[c-1], lis[d-1] = x, x
        c, d = c-1, d + 1

    ###
    teks = ''
    for text in lis:
        teks += '-'.join(text) + '\n'
    print(teks)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)