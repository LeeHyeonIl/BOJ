import sys
from collections import deque
"""
que = deque([(1,2,3,4), (5,5,4,3)])
x1, x2, x3, x4 = que.popleft()
print(x1,x2,x3,x4)
"""

n = int(input())
pipes = [[int(x) for x in sys.stdin.readline().split()] for y in range(n)]



def checkRow(x,y):
    if x >= n:
        return False
    elif pipes[y][x+1] == 1:
        return False
    return True

def checkColumn(x,y):
    if y >= n:
        return False
    elif pipes[y+1][x] == 1:
        return False
    return True

def checkDiagonal(x,y):
    if y >= n or x >= n:
        return False
    if pipes[y+1][x+1] == 1 or pipes[y][x+1] == 1 or pipes[y+1][x] == 1:
        return False
    return True

def bfs():
    queue = deque([(0,1,1),(2,3,3)])
    print(queue)
    direction = [(1,0), (0,1), (1,1)]
    cn = 0

    while queue:
        dx, dy, dd = queue.popleft()
        print(f'dx = {dx} dy = {dy} dd = {dd}')
        if dx == n-1 and dy == n-1:
            cn += 1

        if dd == 1:
            if checkRow(dx, dy):
                queue.append([(dx,dy,1)])
            if checkDiagonal(dx,dy):
                queue.append([(dx,dy,3)])
        
        elif dd == 2:
            if checkColumn(dx, dy):
                queue.append([(dx,dy,2)])
            if checkDiagonal(dx,dy):
                queue.append([(dx,dy,3)])

        elif dd == 3:
            if checkRow(dx, dy):
                queue.append([(dx,dy,1)])
            if checkColumn(dx, dy):
                queue.append([(dx,dy,2)])
            if checkDiagonal(dx,dy):
                queue.append([(dx,dy,3)])
    return cn

print(bfs())
