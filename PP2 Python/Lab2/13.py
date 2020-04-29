def n(a):
    d = dict()
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    cnt = 0
    for i in d.values():
        if i % 2 == 1:
            cnt += 1
        if cnt > 1:
            return False
    return True


a = [int(i) for i in input().split()]

if n(a) == True:
    print("Yes")
else:
    print("No")
