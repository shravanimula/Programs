def palindrome(n):
    temp=n
    rev=0
    while(n > 0):
        rev=rev*10 + n%10
        n=n//10
    if rev==temp:
        return 0
    else:
        return 1
number=int(input("enter a number:"))
result=palindrome(number)
if result==1:
    print("given number not a palindrome")

else:
    print("given number is palindrome")
