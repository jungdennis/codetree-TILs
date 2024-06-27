# def merge(arr1, arr2):
#     arr_merge = []

#     for i in range(len(arr1) + len(arr2)):
#         if len(arr1) == 0:
#             arr_merge.append(arr2.pop(0))
#         elif len(arr2) == 0:
#             arr_merge.append(arr1.pop(0))
#         else:
#             if arr1[0] <= arr2[0]:
#                 arr_merge.append(arr1.pop(0))
#             else:
#                 arr_merge.append(arr2.pop(0))

#     return arr_merge

# def merge_sort(arr, low, high):
#     if low < high:
#         mid = (low + high) // 2
#         arr1 = merge_sort(arr, low, mid)
#         arr2 = merge_sort(arr, mid+1, high)
#         return merge(arr1, arr2)
#     else:
#         return [arr[low]]

# n = int(input())

# arr = list(map(int, input().split()))
# arr = merge_sort(arr, 0, len(arr)-1)
# arr = list(map(str, arr))
# print(" ".join(arr))

def merge(low, mid, high):
    i = low
    j = mid + 1
    k = low

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            arr_merge[k] = arr[i]
            i += 1
        else:
            arr_merge[k] = arr[j]
            j += 1

        k += 1

    while i <= mid:
        arr_merge[k] = arr[i]
        i += 1
        k += 1
    
    while j <= high:
        arr_merge[k] = arr[j]
        j += 1
        k += 1

    for k in range(low, high+1):
        arr[k] = arr_merge[k]

def merge_sort(low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(low, mid)
        merge_sort(mid+1, high)
        merge(low, mid, high)

n = int(input())
arr = list(map(int, input().split()))
arr_merge = [0] * n

merge_sort(0, n-1)

for i in arr:
    print(i, end=' ')