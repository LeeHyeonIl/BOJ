import sys
n = int(input())
a = [(0,0)]
k = 0
cn = 0


for i in range(n):
    s, f = map(int, sys.stdin.readline().split())
    a.append((s,f))
a.sort(key=lambda x:(x[1],x[0]))

for j in range(1,n+1):
    if a[k][1] <= a[j][0]:
        cn += 1
        k = j

print(cn)
