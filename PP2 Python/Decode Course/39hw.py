x=int(input())
#s=-1
list=[1,12,3,4,46,89,0]
list.sort()
print(list)
def check(x,list):
    s=0
    index=-1
#     s=list.index(x)
#     if(s!=-1):
#         print("Есть и находится под индексом",s)
#     else:
#         print("Не найден")
# check(x,list)
    for i in range(len(list)):
        if(list[i]==x):
            s=s+1
            index=i
        if(s!=0):
             print("есть и находится под индексом",index)
        else:
             print("нету")   
check(x,list)

