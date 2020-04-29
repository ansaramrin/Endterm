def ind(a,b):
    res=set(a).intersection(set(b))
    return res
print(ind([1,2,3,4,5],[5,9,8,4]))