def fibnaci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    
    return (fibnaci(n-1)+fibnaci(n-2))

number=int(input("enter a number:"))
result=fibnaci(number)
print("fibnaci result:",result)
