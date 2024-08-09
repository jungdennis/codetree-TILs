n = int(input())
arr = []
possible = []

def check_impossible(arr):
    if len(arr) <= 1:
        return False
    else:
        for i in range(1, len(arr) // 2 + 1):
            arr1 = arr[len(arr)-2*i:len(arr)-i]
            arr2 = arr[len(arr)-i:len(arr)]
            
            if arr1 == arr2:
                return True

        return False

def make_array(x):
    if check_impossible(arr):
        return

    if x >= n:
        # print(arr)
        ans = 0
        for i in range(len(arr)):
            ans += arr[i] * (10 ** i)
        possible.append(ans)
        return

    for num in [4, 5, 6]:
        # if x >= 1 and check_impossible(arr + [num]):
        #     continue

        arr.append(num)
        make_array(x+1)
        arr.pop()

make_array(0)
print(possible[0])