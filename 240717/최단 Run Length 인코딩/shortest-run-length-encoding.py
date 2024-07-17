import sys

def encoding(A):
    encoding_result = ''
    temp = A[0]
    cnt = 1

    for c in A[1:]:
        if temp == c:
            cnt += 1
        else:
            encoding_result += (temp + str(cnt))
            temp = c
            cnt = 1
    encoding_result += (temp + str(cnt))

    return len(encoding_result)

A = sys.stdin.readline().rstrip()

min_length = 20

for i in range(len(A)):
    A = A[-1] + A[:-1]
    encoding_length = encoding(A)

    if encoding_length < min_length:
        min_length = encoding_length

print(min_length)