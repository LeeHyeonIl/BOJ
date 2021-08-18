from collections import deque
n, k = map(int, input().split())
queue = [int(x) for x in range(0, n+1)]
result = []
j = k

while len(result) < n:
    if n >= j:
        if queue[j] == 0:
            j += 1
            continue
        result.append(queue[j])
        queue[j] = 0
    else:
        if queue[j%n] == 0:
            j += 1
            continue
        result.append(queue[j%n])
        queue[j%n] = 0
    j += k
print(result)