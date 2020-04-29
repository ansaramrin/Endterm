import random
list=[]
for i in range(5):
    x=random.randint(1,10)
    list.append(x)
print(list)
maxi=max(list)
mini=min(list)
indMax=list.index(maxi)
indMin=list.index(mini)
list[indMax]=mini
list[indMin]=maxi
print(list)

