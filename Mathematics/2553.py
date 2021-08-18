n = int(input())
j = 0
k = 1

for i in range(2, n+1):
    j = i
    while j % 10 == 0:
        j //= 10
    
    k = k * j
    while k % 10 == 0:
        k //= 10

    k %= 10000000


print(k%10)
