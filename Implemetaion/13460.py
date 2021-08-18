'''
    삼성 SW 역량테스트 기출 문제
    1. 구슬 탈출
        Input)
            첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다. 다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다. 
            이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다. '.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 'O'는 구멍의 위치를 의미한다. 
            'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.
            입력되는 모든 보드의 가장자리에는 모두 '#'이 있다. 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.
        
        Output)
            최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다. 만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.
'''
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
beads = [[x for x in input().split()] for y in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
solve = False
result = -1


# R과 B 그리고 O의 좌표 저장
for i in range(n):
    for j in range(m):
        if beads[i][j] == 'B':
            bx, by = j, i
        elif beads[i][j] == 'R':
            rx, ry = j, i
        elif beads[i][j] == 'O':
            ox, oy = j, i
        else:
            pass

# 10번의 반복시도

for chance in range(1, 11):
    # 4방향중 방향 결정
    for i in range(4):
        ddx = rx + dx[i]
        ddy = ry + dy[i]
        if beads[ddy][ddx] == '#' or beads[ddy][ddx] == 'B':
            continue
        else:
            direction = i
    
    # 결정된 방향으로 전진
    while True:
        rx = rx + dx[direction]
        ry = ry + dy[direction]

        # 빨간 구슬의 움직임
        if beads[ry][rx] == '#':
            break
        elif beads[ry][rx] == 'O':
            solve = True
            result = chance
            break
        else:
            pass

        # 파란 구슬의 움직임
        if beads[by][bx] == '#':
            continue
        
        bx = bx + dx[direction]
        by = by + dy[direction]

        elif beads[by][bx] == 'O':
            

        
    
    if solve:
        break

