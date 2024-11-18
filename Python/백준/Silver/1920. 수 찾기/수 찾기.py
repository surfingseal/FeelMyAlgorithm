n = int(input())
l1 = list(map(int, input().split()))
l1.sort()

m = int(input())
l2 = list(map(int, input().split()))

def l2_in_l1(e):
    first = 0
    last = n - 1
    mid = (first + last) // 2

    while first <= last:
        if l1[mid] == l2[e]:
            return 1

        if l1[mid] < l2[e]:
            first = mid + 1
            mid = (first + last) // 2
        else:
            last = mid - 1
            mid = (first + last) // 2
    return 0

for i in range(m):
    print(l2_in_l1(i))