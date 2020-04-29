list=[1,4,15,3,8]
even=0
odd=0
for i in range(len(list)):
    if (list[i]%2==0):
        even=even+1
    else:
        odd=odd+1
print(list)
print(even)
print(odd)
