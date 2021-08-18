from collections import deque

n,m,v = map(int, input().split())
graph = [[] for y in range(n+1)]



for i in range(m):
    r1, r2 = map(int, input().split())
    graph[r1].append(r2)

pgraph = graph
pgraph.sort(key= lambda x: max(x[1]))
print(pgraph)


visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

def dfs(pgraph, v):
    visited1[v] = True
    print(v, end=' ')

    for j in pgraph[v]:
        if visited1[j] == False:
            dfs(graph, j)

def bfs(pgraph, v):
    queue = deque([v])
    visited2[v] = True

    while queue:
        j = queue.popleft()
        print(j, end=' ')

        for i in pgraph[j]:
            if visited2[i] == False:
                print(i, end=' ')
                queue.append(i)
                visited2[i] = True

dfs(pgraph, v)
print()
bfs(pgraph, v)