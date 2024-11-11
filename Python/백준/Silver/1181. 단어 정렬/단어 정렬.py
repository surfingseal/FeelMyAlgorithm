w_list = []
for i in range(50):
    w_list.append([])

n = int(input())

for i in range(n):
    w = input()

    if w in w_list[len(w) - 1]:
        pass
    else:
        w_list[len(w) - 1].append(w)

    for j in range(50):
        w_list[j].sort()

for i in range(50):
    if w_list[i]:
        for k in range(len(w_list[i])):
            print(w_list[i][k])