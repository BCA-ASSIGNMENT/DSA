x = [4, -2, 8, 9, -12, 14, 11,  16]
count = 0
for i in x:
    if i < 0:
        count = count + 1
print("The count of negative numbers in the array is:", count)
#############################################################
x = [4, -2, 8, 9, -12, 14, 11, 16]
max_num = 0
for i in x:
    if i > max_num:
        max_num = i
print("The maximum number in the array is:", max_num)
#############################################################
x = [4, -2, 8, 9, -12, 14, 11, 16]
min_num = 0
for i in x:
    if i < min_num:
        min_num = i
print("The minimum number in the array is:", min_num)
#############################################################
x = [4, -2, 8, 9, -12, 14, 11, 16]
pos=0
y=9
for i in x:
    if i == y:
        print("The number", y, "is found at position", pos)
    pos =pos + 1