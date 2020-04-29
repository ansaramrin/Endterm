import random
list=[]
even=0
odd=0
for i in range(0,20):
    x=random.randint(0,20)
    list.append(x)
    if (list[i]%2==0):
        even=even+1
    else:
        odd=odd+1
print(list)
print(even)
print(odd)