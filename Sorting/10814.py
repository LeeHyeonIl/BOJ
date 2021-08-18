n = int(input())
members = []
for i in range(n):
    age, name = map(str, input().split())
    members.append((int(age), name, i))

members.sort(key= lambda x :(x[0],x[2]))
for i in range(len(members)):
    print(members[i][0], members[i][1])