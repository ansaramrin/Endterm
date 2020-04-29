def n(a, int):
    s = set()
    for i in a:
        if i > int:
            s.add(i)
    return s
    
a = [int(i) for i in input().split()]
i = int(input())
print(n(a, i))
