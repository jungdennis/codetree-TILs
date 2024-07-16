n, k, T = input().split()

n = int(n)
k = int(k)

arr = []

for i in range(n):
    word = input()
    if word.startswith(T):
        arr.append(word)

arr.sort()
print(arr[k-1])