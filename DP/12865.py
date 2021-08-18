n, k = map(int, input().split())
w = [int(0) for x in range(n+1)]
v = [int(0) for x in range(n+1)]
dp = [0] * (k+1)

for i in range(1,n+1):
    w[i], v[i] = map(int, input().split())

for i in range(1, n+1):
    for j in range(k,1,-1):
        if j >= w[i]:
            dp[j] = max(dp[j], dp[j-w[i]]+ v[i])
        
print(dp[k])
