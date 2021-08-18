from collections import deque

n = int(input())
j = True


for i in range(n):
    process = deque([x for x in input()])
    l = int(input())
    ex = [x for x in input()]
    numbers = deque(ex[1::2])
    for p in process:
        print(p)
        if p == 'R':
            numbers.reverse()
        else:
            if len(numbers) == 0:
                j = False
                break
            else:
                numbers.popleft()
    if not j:
        print('error')
        j = True
    else:
        print('[')
        for i in range(len(numbers)-1):
            print(str(i)+',', end='')
        print(numbers[0])
