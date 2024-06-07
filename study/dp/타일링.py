n = int(input())

p[1] = 1

dp[2] = 2
dp[3] = 3
dp[4] = 


dp[n] = dp[n-1] + dp[n-2]

dp = [0]*1001

dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 100007

print(dp[n]%100007)


