n,r,c = map(int, input().split())

# 해당 행과 열에 대해 구역을 반환해주는 함수
def IsArea(depth, x, y, areaNumber):
    if depth == 2: