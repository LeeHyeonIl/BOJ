while True:
    A = list(str(input()))
    if A[0] == '0':
       break
    try:
        if list(reversed(A)) == A:
            print("yes")
        else:
            print("no")
    except:
        if len(A) == 0:
            break