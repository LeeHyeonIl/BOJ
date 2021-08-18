n = int(input())

cost = [[0 for x in range(3)] for y in range(n+1)]
dp = [[0 for x in range(3)] for y in range(n+1)]

for y in range(1, n+1):
    costs = map(int, input().split())
    x = 0
    for c in costs:
        cost[y][x] = c
        x += 1

for i in range(1, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[n][0], dp[n][1], dp[n][2]))