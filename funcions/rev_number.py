def rev_num(n):
    rev=0
    while(n > 0):
        rev=rev*10 + n%10
        n=n // 10

    return rev

number=int(input("enter a number:"))
print("before reverse the number is:",number)
result=rev_num(number)
print("after reverse the number is:",result)
