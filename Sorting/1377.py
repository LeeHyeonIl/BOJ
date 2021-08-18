import sys
input = sys.stdin.readline

change = False
n = int(input())
array = [0]


for i in range(n):
    array.append(int(input()))

for i in range(1, n+1):
    change = False
    for j in range(1,n-i+1):
        if array[j] > array[j+1]:
            change = True
            t = array[j]
            array[j] = array[j+1]
            array[j+1] = t
    
    if not change:
        print(i)
        break
