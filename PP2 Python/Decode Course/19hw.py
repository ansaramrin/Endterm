n=int(input())
even=0
odd=0
while n>0:
    digit=n%10
    if digit%2==0:
        even=even+1
    else:
        odd=odd+1
    n=n//10
print(even)
print(odd)


    
    