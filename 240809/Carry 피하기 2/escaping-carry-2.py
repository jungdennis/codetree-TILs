n = int(input())
nums = []
for i in range(n):
    nums.append(input())

def check_carry(a, b, c):
    length = max(len(a), len(b), len(c))

    a = a.zfill(length)
    b = b.zfill(length)
    c = c.zfill(length)

    for i in range(length):
        if int(a[i]) + int(b[i]) + int(c[i]) >= 10:
            return False

    return True

max_result = -1
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if check_carry(nums[i], nums[j], nums[k]):
                result = int(nums[i]) + int(nums[j]) + int(nums[k])
                max_result = max(result, max_result)

print(max_result)