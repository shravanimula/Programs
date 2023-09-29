#function without arguments and with return value
def function():
    a=int(input("enter a number:"))
    b=int(input("enter b number:"))
    result=a-b
    print("function without argument and with return value")
    return result

sub=function()
print("result of two variables is:",sub)
