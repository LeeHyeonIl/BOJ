from collections import deque
n = int(input())
cards = deque([int(x) for x in input().split()])
cards.appendleft(0)
dp = [0 for x in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] =  max(dp[i-j]+cards[j], dp[i])

print(dp[n])