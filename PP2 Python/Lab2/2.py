def even(lst):
    mass=[]
    for i in range(len(lst)):
        if i%2==0:
            mass.append(lst[i])
    return mass
list1=list(map(int,input().split()))
print(even(list1))
