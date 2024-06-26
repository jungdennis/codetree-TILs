n = int(input())
arr = list(map(int, input().split()))

sorted = False

while sorted == False:
    sorted = True

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            temp = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = temp
            sorted = False

arr = list(map(str, arr))
print(" ".join(arr))