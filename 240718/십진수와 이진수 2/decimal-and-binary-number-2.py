def to_decimal(binary):
    binary = list(map(int, list(binary)))
    decimal = 0

    for b in binary:
        decimal = decimal * 2 + b

    return decimal

def to_binary(decimal):
    binary = []

    while 1:
        binary.append(decimal % 2)
        decimal = decimal // 2

        if decimal <= 0:
            break

    for b in binary[::-1]:
        print(b, end='')


binary = input()
decimal = to_decimal(binary)
to_binary(decimal * 17)