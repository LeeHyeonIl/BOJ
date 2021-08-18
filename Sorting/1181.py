from collections import Set
n = int(input())
sol = []
for i in range(n):
    word = input()
    sol.append(word)

sol = list(set(sol))
sol.sort(key=lambda x:(len(x), x))
for s in sol:
    print(s)