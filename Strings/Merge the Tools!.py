def merge_the_tools(string, k):
    # your code goes here
    for i in zip(*[iter(string)] * k): # Cara mengsplit string menjadi n/k bagian (Masing2 bagian panjangnya k)
        teks = ''
        for x in i:
            teks += x if x not in teks else ''
        print(teks)

merge_the_tools('AABCAAADA', 3)
