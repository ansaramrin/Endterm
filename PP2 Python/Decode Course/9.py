a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))
max1=0
min1=0
mid=0
if a>b and a>c:
 max1=a
elif b>a and b>c:
 max1=b
elif(c>a and c>b):
 max1=c

if a<b and a<c:
 min1=a
elif b<a and b<c:
 min1=b
elif(c<a and c<b):
 min1=c

if a!=max1 and a!=min1:
 mid=a
elif b!=max1 and b!=min1:
 mid=b
elif c!=max1 and c!=min1:
 mid=c

print("max=",max1," mid=",mid," min1=",min1)