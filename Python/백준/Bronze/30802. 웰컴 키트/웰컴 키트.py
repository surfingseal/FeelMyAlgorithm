n =  int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
count1, count2, count3 = 0, 0, 0
for i in range(6):
    if not size[i]:
        pass
    elif size[i] <= t:
        count1 += 1
    elif size[i] % t == 0:
        count1 += size[i] // t
    else:
        count1 += size[i] // t + 1

count2 = n // p
count3 = n % p

print(count1)
print(count2, count3)
