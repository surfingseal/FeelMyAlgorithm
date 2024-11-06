while True:
    tri_list = list(map(int, input().split()))
    if 0 in tri_list:
        break
    tri_list.sort()
    
    if tri_list[0] ** 2 + tri_list[1] ** 2 == tri_list[2] ** 2:
        print("right")
    else:
        print("wrong")