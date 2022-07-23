def minion_game(s):
    frb = ['A', 'E', 'I', 'O', 'U']
    kevin = 0
    stuart = 0
    for i in range(len(s)):
        if s[i] not in frb:
            stuart += len(s)-i # Amazing math in combinations
        else:
            kevin += len(s)-i
    if kevin > stuart:
        print('Kevin', kevin)
    elif stuart > kevin:
        print('Stuart', stuart)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)