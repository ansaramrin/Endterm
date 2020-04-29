import random
x=int(input())
y=int(input())
lst=[]
def func(x,y):
    for i in range(10):
        lst.append(random.randint(x,y))
func(x,y)
print(lst)