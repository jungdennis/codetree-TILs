n = int(input())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print("Yes") if A == B else print("No")