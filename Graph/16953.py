a, b = map(int, input().split())
cnt = 1

while True:
    
    
    if b % 2 == 0:
        b = b / 2
    
    else:
        b -= 1
        b /= 10
    cnt += 1

    if a >= b:
        break

if b < a:
    print(-1)
else:
    print(cnt)