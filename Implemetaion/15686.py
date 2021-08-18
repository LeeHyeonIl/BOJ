'''
    curve는 커브 상태를 나타내기 위한 배열, 좌표가 포함된다면 1 아니면 0으로 표현
'''
#1. 0세대 드래곤 커브 구현
#2. 1세대 드래곤 커브 구현
#3. 튜플을 이용하여 배열처리

curve = [[0 for x in range(10)] for y in range(10)]

n = int(input())
dx = [1,0,-1,0]
dy = [0,-1,0,1]


for i in range(n):
    x, y, d, g = map(int, input().split())
    depth = 0
    queue = [] 
    while depth <= g:
        if depth == 0:
            queue.append((x,y),(x+dx[d], y+dy[d]))
        else:
            mx, my = queue[-1]
            for q in queue:
                x1, y1 = q
                queue.appeend((x1+(my-y1)))



        


print(curve)


