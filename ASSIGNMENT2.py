#PRINT 1 TO 10 USING RECURSION FUNCTION WHERE INPUT WLL BE TAKEN FROM USER
def range(a, b):
    if a == b:
        return a
    else:
        return a + range(a+1, b)
a=int(input("ENTER THE STARTING NUMBER:"))
b=int(input("ENTER THE ENDING NUMBER:"))
ok=range(a,b)
print(ok)
#PRINT 1 TO 10 USING RECURSION FUNCTION
def print_numbers(n):
    if n <= 10:
        print(n)
        print_numbers(n+1)
print_numbers(1)
#PRINT FACTORIAL OF A GIVEN NUMBER USING RECURSION FUNCTION
def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)
result=fac(5)
print(result)
#print the summation of 1 to 10 using recursion function
def range(a, b):
    if a == b:
        return a
    else:
        return a + range(a+1, b)
ok=range(1, 10)
print(ok)