

while True:
    number = input()
    if number == 0:
        break

    for i in range(len(number)//2):
        if number[i] != number[len(number)//2-i]:
            print("no")
            break
        if i == len(number) // 2 - 1:
            print("yes")            