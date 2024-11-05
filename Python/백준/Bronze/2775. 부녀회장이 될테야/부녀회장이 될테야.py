t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())

    apt = [[j + 1 for j in range(n)]]

    for floor in range(k):
        apt_floor = []

        for room in range(n):
            sum = 0

            for count in range(room + 1):
                sum += apt[floor][count]
            apt_floor.append(sum)
        apt.append(apt_floor)

    print(apt[k][n - 1])
