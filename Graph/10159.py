import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())
v = []
graph = [[INF for x in range(n+1)]for y in range(n+1)]
graph1 = [[INF for x in range(n+1)]for y in range(n+1)]
graph2 = [[INF for x in range(n+1)]for y in range(n+1)]


for i in range(1, n+1):
    graph1[i][i] = graph2[i][i] = 0

for t in range(m):
    v1,v2 = map(int, input().split())
    graph1[v1][v2] = graph2[v2][v1] = 1


for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph1[j][k] = min(graph1[j][k], graph1[j][i]+graph1[i][k])

for t in range(m):
    graph2[v2][v1] = 1 

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph2[j][k] = min(graph2[j][k], graph2[j][i]+graph2[i][k])

print(graph1)
print(graph2)

for i in range(1, n+1):
    for j in range(1, n+1):
        graph[i][j] = min(graph1[i][j], graph2[i][j])

for g in range(1, n+1):
    print(graph[g].count(INF)-1)