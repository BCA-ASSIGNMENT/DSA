######################################
#IMPLEMENTATION OF BINARY SEARCH
######################################
x = [2, 4, 10, 18, 20, 22, 32, 34]
y = int(input("Enter a number: "))
low = 0
high = len(x) - 1
while low <= high:
    mid = (low + high) // 2  
    if x[mid] == y:  
        print("Found y at index", mid)
        break
    if x[mid] < y:
        low = mid + 1
    elif x[mid] > y:
        high = mid - 1
else:
    print("y not found")
######################################
#IMPLEMENTATION OF SEQUENTIAL SEARCH
######################################
x = [2, 4, 10, 18, 20, 22, 32, 34]
y = int(input("Enter a number: "))
for i in range(len(x)):
    if x[i] == y:
        print("Found y at index", i)
        break
else:
    print("y not found")
