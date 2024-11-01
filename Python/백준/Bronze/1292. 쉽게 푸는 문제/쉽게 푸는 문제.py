a, b= input().split()
a = int(a)
b = int(b)

count = 0
switch = 0
sum = 0

for i in range(1, 1001):
    for j in range(1, i + 1):
        count += 1
        if count == a:
            switch = 1
        if switch == 1:
            sum += i
        if count == b:
            switch = 2
            break

    if switch == 2:
        break

print(sum)


