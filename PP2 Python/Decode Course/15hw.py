a=int(input())
b=int(input())
c=int(input())
if a>=b+c or b>=a+c or c>=a+b:
    print("Такой треугольник не существует.")
elif a!=b and a!=c and b!=c:
    print("Это разносторонний треугольник.")
elif (a==b and c!=a and c!=b) or (a==c and b!=a and b!=c) or (b==c and a!=b and a!=c):
    print("Это равнобедренный треугольник.")
elif a==b and a==c and b==c:
    print("Это равносторонний треугольник.")