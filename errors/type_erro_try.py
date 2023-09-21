a=int(input("enter  number:"))
b=input("enter the input:")
try:
    result=a+b
except TypeError:
    print("cannot add to different variable")
