import math
n,p,q = map(int, input().split())
dp = [1 for x in range(n+1)]

for i in range(1,n+1):
    dp[i] = dp[int(math.floor(i/p))] + dp[int(math.floor(i/q))]
print(dp[n])