# def merge(arr, low, mid, high):
#     arr_merge = []
#     arr1 = arr[low:mid]
#     arr2 = arr[mid:high]

#     for i in range(len(arr1) + len(arr2)):
#         if arr1[0] <= arr2[0] or len(arr2) == 0:
#             arr_merge.append(arr1.pop(0))
#         elif arr1[0] > arr2[0] or len(arr1) == 0:
#             arr_merge.append(arr2.pop(0))

#     return arr_merge

def merge(arr1, arr2):
    arr_merge = []

    for i in range(len(arr1) + len(arr2)):
        if len(arr1) == 0:
            arr_merge.append(arr2.pop(0))
        elif len(arr2) == 0:
            arr_merge.append(arr1.pop(0))
        else:
            if arr1[0] <= arr2[0]:
                arr_merge.append(arr1.pop(0))
            else:
                arr_merge.append(arr2.pop(0))

    return arr_merge

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        arr1 = merge_sort(arr, low, mid)
        arr2 = merge_sort(arr, mid+1, high)
        return merge(arr1, arr2)
    else:
        return [arr[low]]

n = int(input())

arr = list(map(int, input().split()))
arr = merge_sort(arr, 0, len(arr)-1)
arr = list(map(str, arr))
print(" ".join(arr))