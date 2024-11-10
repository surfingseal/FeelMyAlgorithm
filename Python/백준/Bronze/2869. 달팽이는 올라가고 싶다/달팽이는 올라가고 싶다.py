a, b, v = map(int, input().split())
day = 0
d = a - b

if a == v:
    day = 1

elif v % d == 0:
    day = v // d - a // d + 1

else:
    if v % d > a % d:
        day = v // d - a // d + 2
    else:
        day = v // d - a // d + 1

print(day)