n = int(input())
LEN = 6000000
prime = [True for i in range(LEN)]

for i in range(2,LEN):
    if prime[i] == False:
        continue
    for j in range(i+i,LEN,i):
        prime[j] = False

def IsPalin(n):
    target = list(n)
    if target[0] == '0':
        return False
    if list(reversed(target)) == target:
        return True
    else:
        return False

if n <= 2:
    print(2)
else:
    for i in range(len(prime)):
        if i < n or not prime[i]:
            continue
        if IsPalin(str(i)):
            print(i)
            break






