while True:
    n = int(input())
    if n == 0:
        break

    if n // 10 == 0:
        print('yes')
    elif n // 100 == 0:
        n1 = n % 10
        n2 = n // 10

        if n1 == n2:
            print('yes')
        else:
            print('no')
    elif n // 1000 == 0:
        n1 = n % 10
        n3 = n // 100

        if n1 == n3:
            print('yes')
        else:
            print('no')
    elif n // 10000 == 0:
        n1 = n % 10
        n2 = (n // 10) % 10
        n3 = (n // 100) % 10
        n4 = n // 1000

        if n1 == n4 and n2 == n3:
            print('yes')
        else:
            print('no')
    else:
        n1 = n % 10
        n2 = (n // 10) % 10
        n4 = (n // 1000) % 10
        n5 = n // 10000

        if n1 == n5 and n2 == n4:
            print('yes')
        else:
            print('no')