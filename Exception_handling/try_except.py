a=int(input("enter number:"))
b=input("enter a string:")
try:
    result=a+b
except TypeError:
    print("cannot add int and string")
