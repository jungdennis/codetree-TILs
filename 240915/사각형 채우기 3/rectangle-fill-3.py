n = int(input())

dp = [0] * (n+1)

for i in range(n+1):
    if i <= 1:
        dp[i] = 1
    else:
        dp[i] = dp[i-1] + dp[i-2]

ans = dp[n] * (2 ** n - 1) + 1
print(ans % 1000000007)