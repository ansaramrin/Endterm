s=int(input("Сумма"))
p=float(input("Процент"))
n=int(input("Лет"))
m=(s*p*(1+p)**n)/(12*((1+p)**n-1))*12*10*100/1000000
print(m,end='%')