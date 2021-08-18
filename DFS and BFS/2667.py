n = int(input())
houses = [[int(x) for x in input()] for y in range(n)]
visited = [[False for x in range(n)] for y in range(n)]
cnt = 0
w = 1
numbers = []

def bfs(houses, x, y):
    global w
    visited[x][y] = True

    if checkPoint(x+1,y):
        if not visited[x+1][y] and houses[x+1][y] == 1:
            bfs(houses,x+1,y)
            w+=1
        
    if checkPoint(x,y+1):
        if not visited[x][y+1] and houses[x][y+1] == 1:
            bfs(houses,x,y+1)
            w+=1

    if checkPoint(x-1,y):
        if not visited[x-1][y] and houses[x-1][y] == 1:
            bfs(houses,x-1,y)
            w+=1

    if checkPoint(x,y-1):
        if not visited[x][y-1] and houses[x][y-1] == 1:
            bfs(houses,x,y-1)
            w+=1

def checkPoint(x,y):
    global n
    if x < 0 or y < 0:
        return False
    elif x >= n or y >=n:
        return False
    else:
        return True

for i in range(n):
    for j in range(n):
        if not visited[i][j] and houses[i][j] == 1:
            bfs(houses,i,j)
            cnt+=1
            numbers.append(w)
            w = 1
print(cnt)
numbers.sort()
for n in numbers:
    print(n)