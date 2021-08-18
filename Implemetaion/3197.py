from collections import deque
import time
n, m = map(int, input().split())
river = [[x for x in input()] for y in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
swans = deque()
day = 0

for i in range(n):
    for j in range(m):
        if river[i][j] == 'L':
            swans.append([j,i])

x1, y1 = map(int, list(swans[0]))
x2, y2 = map(int, list(swans[1]))

def IsPossible():
    root = deque()
    root.append((x1,y1))
    visited = [[False for x in range(m)] for y in range(n)]
    while root:
        x, y = root.popleft()
        for k in range(4):
                ddx = x + dx[k]
                ddy = y + dy[k]

                if ddx == x2 and ddy == y2:
                    return True

                if ddy < 0 or ddy >= n or ddx < 0 or ddx >= m:
                    continue

                if river[ddy][ddx] == 'X' or river[ddy][ddx] == 'L':
                    continue

                if river[ddy][ddx] == '.' and visited[ddy][ddx] == False:
                    visited[ddy][ddx] = True
                    root.append((ddx,ddy))              
    return False
"""
def melt():
    for i in range(n):
            for j in range(m):
                if river[i][j] == '.':
                    for k in range(4):
                        ddx = j + dx[k]
                        ddy = i + dy[k]

                        if ddy >= 0 and ddy < n and ddx >= 0 and ddx < m and river[ddy][ddx] == 'X':
                            river[ddy][ddx] = 'O'

    for i in range(n):
            for j in range(m):
                if river[i][j] == 'O':
                    river[i][j] = '.'
"""
def melt():
    root = deque()
    check = False
    number = 1
    for i in range(n):
            for j in range(m):
                if river[i][j] == 'X':
                    x1 = j
                    y1 = i
                    check = True
                    break
            if check:
                break
    
    root.append((x1,y1))
    visited = [[False for x in range(m)] for y in range(n)]

    while root:
        x, y = root.popleft()
        for k in range(4):
                ddx = x + dx[k]
                ddy = y + dy[k]
                print(f"ddx = {ddx} ddy = {ddy}")
                time.sleep(0.01)
                if ddx == m-1 and ddy == n-1:
                    break

                if ddy < 0 or ddy >= n or ddx < 0 or ddx >= m:
                    continue

                if river[ddy][ddx] == 'X':
                    river[ddy][ddx] = number
                    root.append((ddx,ddy))

                elif river[ddy][ddx] == '.' or river[ddy][ddx] == 'L':
                    continue

                else:
                    river[ddy][ddx] = min(river[ddy][ddx],number)
                    root.append((ddx,ddy))
        number += 1

melt()
print(river)


"""
while True:
    if not IsPossible():
        melt()
    else:
        print(day)
        break
    day += 1
"""