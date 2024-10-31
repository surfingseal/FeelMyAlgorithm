sugar = int(input())

bag5 = 0
bag3 = 0

if sugar % 5 == 0:
    bag5 = sugar // 5
    print(bag5)
elif sugar % 3 == 0 and sugar // 3  < 5:
    bag3 = sugar // 3
    print(bag3)
else:
    for i in range(1, 1000):  # x = 5 * i + 3 * j
        if (sugar - 5 * i) >= 0 and (sugar - 5 * i) % 3 == 0 and (sugar - 5 * i) // 3 < 5 :
            bag5 = i
            bag3 = (sugar - 5 * i) // 3
            print(bag5 + bag3)
            break

if bag5 == 0 and bag3 == 0:
    print(-1)

