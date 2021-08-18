n = int(input())
result = 1
for i in range(1,n+1):
    result *= i  
    while result % 10 == 0:
        result //= 10
    result %= 10000000000000
result %= 100000

if result < 10000:
    print(0, end='')
print(result)