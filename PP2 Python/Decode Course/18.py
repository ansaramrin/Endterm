n=int(input())
res=0
for i in range(100000):
    if n>0:
        digit=n%10
        n=n//10
        res=res+digit
        res=res*10
    else:
        print(res//10)
        break

