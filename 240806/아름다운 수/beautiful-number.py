digit = []
cnt = 0
arr = []

n = int(input())

def beautiful(x):
    global cnt

    if x == n:
        cnt += 1
        return
    elif x > n:
        return

    for i in range(1, 5):
        for j in range(i):
            digit.append(i)
        
        beautiful(x+i)
        
        for j in range(i):
            digit.pop()

beautiful(0)
print(cnt)