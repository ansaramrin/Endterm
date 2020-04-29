l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
i1 = int(input('Position: '))
i2 = int(input('Deletes elements after index: '))

def f(l1,l2,i1,i2):
    list=[]
    for i in range(0,i1):
        list.append(l1[i])
    for i in range(0,len(l2)):
        list.append(l2[i])
    for i in range(i1,len(l1)):
        list.append(l1[i])
    for i in range(i2,len(list)):
        list.pop()
    return list

print(f(l1,l2,i1,i2))
    