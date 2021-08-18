n, m = map(int, input().split())
input_data = [int(x) for x in input().split()]
input_data.append(0)
input_data.sort()
visited = [False for x in range(100)]
array = [0 for x in range(100)]

def NM(cnt):
    if cnt == m:
        for i in range(0, m):
            print(array[i], end=' ')
        print()
    else:
        for i in range(1, n+1):
            array[cnt] = input_data[i]

            if cnt >= 1 and array[cnt-1] <= array[cnt] or cnt == 0:
                NM(cnt+1)

NM(0)