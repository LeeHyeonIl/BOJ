n = int(input())
t  = [[]]
dp = [[0 for x in range(n+1)] for y in range(n+1)]
for i in range(n):
    input_data = (list(map(int, input().split())))
    input_data.insert(0,0)
    t.append(input_data)
print(t[1])

dp[1][1] = t[1][1]


for i in range(2, n+1):
    for j in range(1, i+1):
        if j == 1:
            dp[i][j] = dp[i-1][j] + t[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + t[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+t[i][j]


print(max(dp[n]))