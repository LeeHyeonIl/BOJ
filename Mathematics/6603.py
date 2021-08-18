import itertools

while True:
    numbers = [int(x) for x in input().split()]
    if numbers[0] == 0:
        break
    l = list(itertools.combinations(numbers[1:], 6))
    for j in l:
        for s in list(j):
            print(s, end= ' ')
        print()
    print()