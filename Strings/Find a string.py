def count_substring(string, sub_string):
    l = len(sub_string)
    result = 0
    for i in range(len(string)-l+1):
        print(string[i:i+l])
        if sub_string == string[i:i+l]:
            result += 1
    return result



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)