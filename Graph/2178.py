from collections import deque

n, m = map(int ,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int ,input())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y,graph):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]

            if ddx < 0 or ddx >= m or ddy < 0 or ddy >= n:
                continue

            if graph[ddy][ddx] == 0:
                continue

            if graph[ddy][ddx] == 1:
                graph[ddy][ddx] = graph[y][x] + 1
                queue.append((ddx, ddy))

    return graph[n-1][m-1]

print(bfs(0,0,graph))