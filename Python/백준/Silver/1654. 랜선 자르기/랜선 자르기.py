k, n = map(int, input().split())
s = []

for i in range(k):
    s.append(int(input()))

first = 1
last = max(s)
mid = (first + last) // 2
max_length = 0

while first <= last:
    result = 0
    for i in range(k):
        if s[i] >= mid:
            result += s[i] // mid
        else:
            pass

    if result >= n:
        max_length = mid
        first = mid + 1
        mid = (first + last) // 2
    else:
        last = mid - 1
        mid = (first + last) // 2

print(max_length)

