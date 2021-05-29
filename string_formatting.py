def print_formatted(number):
    w = len(str(bin(number))[2:])
    [print(str(x).rjust(w,' '), str(oct(x))[2:].rjust(w,' '), str(hex(x))[2:].rjust(w,' ').upper(), str(bin(x))[2:].rjust(w,' ')) for x in range(1,number+1)]

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
