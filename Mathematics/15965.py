import time

LEN = 7370001
prime = [True for i in range(LEN)]
number = 0
k = int(input())
start = time.time()
for i in range(2,LEN):
    if prime[i] == False:
        continue
    for j in range(i+i,LEN,i):
        prime[j] = False



for i in range(2, LEN):
    if prime[i]:
        number += 1
    else:
        continue

    if number == k:
        print(i)
        break
print(f'number = {number}')
print("time :", time.time() - start)
