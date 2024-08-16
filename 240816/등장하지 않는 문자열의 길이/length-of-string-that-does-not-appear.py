n = int(input())
string = input()

for length in range(1, n+1):
    flag = False

    for i in range(n - length + 1):
        target = string[i:i+length]
        cnt = 0

        for j in range(n - length + 1):
            if string[j:j+length] == target:
                cnt += 1

        if cnt >= 2:
            flag = True

    if not flag:
        print(length)
        break