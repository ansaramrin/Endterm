lst = [int(i) for i in input().split()]
i = int(input())
def f(lst1, ind):
    for i in range(ind,len(lst1)):
        lst.pop()
    return lst1        

print(f(lst, i))