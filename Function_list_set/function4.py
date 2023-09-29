#function with argument and with return value
def function(a,b):
    print("function with argument and with return value")
    result=a*b
    return result
x=int(input("enter the x value:"))
y=int(input("enter the y value:"))
result=function(x,y)
print("multiplication of two numbers is:",result)
