from collections import deque
import collections
import itertools
t = int(input())

for test_case in range(t):
    n,m = map(int, input().split())
    queue = deque([int(x) for x in input().split()])
    target = queue[m]
    target_index = m
    cnt = 1

    while True:
        maxValue = queue[0]
        for idx in range(1, len(queue)):
            if maxValue < queue[idx]:
                maxValue = queue[idx]

        if target_index == 0:
            if queue[0] < maxValue:
                k = queue.popleft()
                queue.append(k)
                target_index = len(queue)-1
            else:
                print(cnt)
                break
        
        else:
            if queue[0] < maxValue:
                k = queue.popleft()
                queue.append(k)
                
            else:
                queue.popleft()
                cnt += 1

            target_index -= 1
        