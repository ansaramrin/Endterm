numbers=[[0,1,2],[3,4,5],[6,7,8]]
numbers2=[[5,6,7],[4,2,1],[8,9,1]]
numbers3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        numbers3[i][j]=numbers[i][j]+numbers2[i][j]       
print(numbers3)


