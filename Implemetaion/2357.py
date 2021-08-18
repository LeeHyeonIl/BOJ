import sys

n, m = map(int, sys.stdin.readline().split())
numbers = []
solution = [[0,0] for x in range(m)]

for i in range(n):
    k = int(sys.stdin.readline())
    numbers.append(k)

for j in range(m):
    r1, r2 = map(int, sys.stdin.readline().split())
    sorted_numbers = numbers[(r1-1):r2]
    solution[j][0] = min(sorted_numbers)
    solution[j][1] = max(sorted_numbers)

for i in range(m):
    print(solution[i][0], solution[i][1])