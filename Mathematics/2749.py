n = int(input())
cycle = 15*(10**(5))

dp = [0 for x in range(cycle+1)]
dp[1] = 1
dp[2] = 1

p = n % cycle

for i in range(3, p+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 1000000

print(dp[p])

