def n(a):
    cnt = 0
    for i in range(0,len(a),2):
        if a[i]%2!=0:
            cnt+=1
    return cnt
a = [int(i) for i in input().split()]
print(n(a))
