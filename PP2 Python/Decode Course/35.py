def convert(a):
    s =" "
    bnr="00000000"
    i=7
    while a!=0:
        bnr[i]=str(a%2)
        a//=2
        i-=1
    return (s.join(bnr))
while True:
    d=int(input("num"))
    if d!=0:
        print(convert(d))
    else:
        break
