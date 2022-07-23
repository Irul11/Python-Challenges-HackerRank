def print_formatted(number):
    # your code goes here
    length = len(bin(number)[2:])
    text = ''
    for i in range(1, number + 1):
        decimal = ' '*(length - len(str(i))) + str(i)
        hexadecimal = ' '*(length - len(hex(i)[2:])) + hex(i)[2:].upper()
        octal = ' ' * (length - len(oct(i)[2:])) + oct(i)[2:]
        binary = ' ' * (length - len(bin(i)[2:])) + bin(i)[2:]
        text += '{} {} {} {}\n'.format(decimal, octal, hexadecimal, binary)
    print(text)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
