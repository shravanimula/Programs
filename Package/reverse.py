def reverse_num(n):
    rev=0
    while(n):
        rev=rev*10+n%10
        n=n//10
    print("reverse the number is:",rev)

