arr = list(map(int, input().split()))
arr.sort()

for a in range(15):
    for b in range(a+1, 15):
        for c in range(b+1, 15):
            for d in range(c+1, 15):
                A, B, C, D = arr[a], arr[b], arr[c], arr[d]

                ans = [A, B, C, D, A + B, B + C, C + D, D + A, A + C, B + D, A + B + C, A + B + D, A + C + D, B + C + D, A + B + C + D]

                if sorted(ans) == arr:
                    print(A, B, C, D)
                    break