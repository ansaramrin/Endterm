t = (int(i) for i in input().split())
def maxinlist(l):
    maxi=0
    for i in range(0,len(l)):
        if maxi<l[i]:
            maxi=l[i]
    return maxi
def mininlist(l):
    mini=10000000
    for i in range(0,len(l)):
        if mini>l[i]:
            mini=l[i]
    return mini
print(mininlist(t), maxinlist(t))
