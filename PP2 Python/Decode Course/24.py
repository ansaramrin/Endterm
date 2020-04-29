list=[-2,5,-6,-7,9,0]
list1=[]
print(list)
for i in range(len(list)):
    if list[i]>0:
        list[i]=1
        list1.append(1)
    elif list[i]<0:
        list[i]=-1
        list1.append(-1)
    else:
        list[i]=0
        list1.append(0)
print(list1)
    

