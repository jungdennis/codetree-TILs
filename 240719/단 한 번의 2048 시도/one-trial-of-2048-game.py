import sys

arr = []
for i in range(4):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

d = sys.stdin.readline().rstrip()

def plus_sort(arr, n=4):
    for j in range(len(arr)-1):
            if arr[j] == arr[j+1]:
                arr[j] = arr[j] * 2
                arr[j+1] = 0

    temp = []
    for j in range(len(arr)):
        if arr[j] != 0:
            temp.append(arr[j])

    return temp + [0 for i in range(n - len(temp))]

if d == "L":
    for i in range(4):
        temp = []
        for j in range(4):
            if arr[i][j] != 0:
                temp.append(arr[i][j])

        temp = plus_sort(temp)

        arr[i] = temp
elif d == "R":
    for i in range(4):
        temp = []
        for j in range(3, -1, -1):
            if arr[i][j] != 0:
                temp.append(arr[i][j])

        temp = plus_sort(temp)

        arr[i] = temp[::-1]
elif d == "U":
    for j in range(4):
        temp = []
        for i in range(4):
            if arr[i][j] != 0:
                temp.append(arr[i][j])

        temp = plus_sort(temp)

        for i in range(4):
            arr[i][j] = temp[i]
elif d == "D":
    for j in range(4):
        temp = []
        for i in range(3, -1, -1):
            if arr[i][j] != 0:
                temp.append(arr[i][j])

        temp = plus_sort(temp)

        for i in range(3, -1, -1):
            arr[i][j] = temp[3-i]


for i in range(4):
    for j in range(4):
        print(arr[i][j], end = ' ')
    print()