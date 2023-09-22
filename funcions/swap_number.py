def swap_num(x,y):
    temp=x
    x=y
    y=temp
    print("after swap the : x=",x,"y=",y)

a=int(input("enter a number:"))
b=int(input("enter b number:"))
print("before swap: a=",a,"b=",b)
swap_num(a,b)
