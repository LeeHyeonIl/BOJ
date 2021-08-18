t = int(input())
for i in range(t):
    m,n,k = map(int, input().split())
    pek = [[0 for x in range(m)] for y in range(n)]

    for j in range(k):
        r1, r2 = map(int, input().split())
        pek[r1][r2] = 1
    
    