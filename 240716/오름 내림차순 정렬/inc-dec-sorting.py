n = int(input())
arr = list(map(int, input().split()))

arr_up = list(map(str, sorted(arr)))
arr_down = list(map(str, sorted(arr, reverse=True)))

print(" ".join(arr_up))
print(" ".join(arr_down))