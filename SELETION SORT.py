data=[2,4,18,-5,7,12,3,9,6]
for i in range (0,len(data)):
    for j in range (i+1,len(data)):
        if data[i]>data[j]:
            temp=data[i]
            data[i]=data[j]
            data[j]=temp
print(data)