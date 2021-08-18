n, m = map(int, input().split())
input_data = [int(x) for x in input().split()]
input_data.append(0)
input_data.sort()
visited = [False for x in range(n+1)]
array = [0 for x in range(n+1)]

def NM(cnt):
    if cnt == m:
        for i in range(0, m):
            print(array[i], end=' ')
        print()
    
    for i in range(1, n+1):
        if not visited[i]:
            array[cnt] = input_data[i]
            visited[i] = True
            if cnt >= 1 and array[cnt-1] < array[cnt] or cnt == 0:
                NM(cnt+1)
            visited[i] = False

NM(0)