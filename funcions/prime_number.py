def prime_num(n):
    flag=0
    for i in range(2,n//2):
        if n%i==0:
            flag=1
            break
        
    return flag

number=int(input("enter a number:"))
result=prime_num(number)
if result==1:
    print(number ,"is not a prime")
else:
    print(number,"is prime")

