def add(m,n):
    r=m+n
    print("add is:",r)

def sub(x,y):
    r=x-y
    print("sub is:",r)

def multi(a,b):
    r=a*b
    print("multiplication is:",r)

def divi(m,n):
    r=m/n
    print("division is :",r)

def floor(x,y):
    z=x//y
    print("the floor divison is:",z)

a=int(input('enter the a variable:'))
b=int(input('enter the b variable:'))
print("sum of the two variable:",a+b)
print("subtraction of two variable:",a-b)
print("multiplication of two variable:",a*b)
print("power of two numbers:",a**b)
print("division of two numbers:",a/b)
print('floor divison of two numbers:',a//b)
print('modules of two numbers:',a%b)
add(a,b)
sub(a,b)
multi(a,b)
divi(a,b)
floor(a,b)
