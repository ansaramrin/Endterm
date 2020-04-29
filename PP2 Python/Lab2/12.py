def n(a):
    a.sort()
    s = set()
    s.add(a[0])
    s.add(a[1])
    for i in a:
        q = False
        for j in s:
            if i == j:
                q = True
        if q == True:
            s.add(i*i)
        else:
            s.add(i)
    return s

a = [int(i) for i in input().split()]
print(n(a))
