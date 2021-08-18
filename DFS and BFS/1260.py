from collections import deque
n,m,v = map(int, input().split())
graph = [[] for y in range(n+1)]

for i in range(m):
    r1,r2 = map(int, input().split())
    graph[r1].append(r2)
    graph[r2].append(r1)

for i in graph:
    i.sort()

visited = [False] *(n+1)


def dfs(graph, v):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i)

def bfs(graph, v):
    print(v, end=' ')
    visited[v] = True
    queue = deque([v])
    while queue:
        j = queue.popleft()
        for i in graph[j]:
            if not visited[i]:
                print(i, end=' ')
                visited[i] = True             
                queue.append(i)


dfs(graph, v)
print()
visited = [False] *(n+1)
bfs(graph, v)
