import random
maxarr=[]
arr=[]
maxIndex=1
def summa():
    a=[]
    for i in range(10):
        a.append(int(random.randint(1,15)))
    print(a,sum(a))
    return a
for i in range(10):
    arr=summa()
    if(sum(maxarr)<sum(arr)):
        maxarr=arr
        maxIndex=i+1
print(maxarr,maxIndex)