def reverse(lst): 
    lst.reverse() 
    return lst
lst = [int(i) for i in input().split()]
print(reverse(lst)) 