n = int(input())
fibo = [0 for x in range(n+3)]
fibo[0] = 0
fibo[1] = fibo[2] = 1

for i in range(3,n+1):
    fibo[i] = (fibo[i-1] % 1000000007 + fibo[i-2] % 1000000007) % 1000000007

print(fibo[n])