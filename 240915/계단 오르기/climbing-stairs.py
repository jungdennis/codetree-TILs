n = int(input())

dp = [0] * (n+1)

for i in range(n+1):
    if i == 2 or i == 3:
        dp[i] = 1
    elif i >= 3:
        dp[i] = dp[i-3] + dp[i-2]


print(dp[n] % 10007)