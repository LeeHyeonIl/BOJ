k, n = map(int, input().split())
numbers = [int(x) for x in input().split()]
m = []


for i in range(k):
    for j in range(k):
        m.append(numbers[i] * numbers[j])

for i in numbers:
    m.append(i)

m = set(m)
m = list(m)
m.sort()
print(m)