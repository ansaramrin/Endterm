import random
list1=[]
list2=[]
list3=[]
for i in range(0,6):
    x=random.randint(1,7)
    list1.append(x)
    list2.append(int(input("numbers")))
    list3.append(list1[i]+list2[i])
print(list1)
print(list2)
print(list3)