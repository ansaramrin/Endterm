list = [5,3,-1,8,0,-6,1]
res=0
for i in range(len(list)):
    if(list[i]<0):
        ind=list.index(list[i])
        break
for i in range(ind+1,len(list)):
    if(list[i]<0):
        list[i]=list[i]*-1
    res=res+list[i]
print(res)

