#Check it its alnum then add s1
s=input()
print(s)
s1=' '
for i in s:
    if i.isalnum():
        s1+=i
print(s1)

s2=' '
for i in s1:
    if i.isalpha():
        s2+=i
print(s2)

s3=' ' 
for i in s2:
    if i.isupper():
        s3=s3+i.lower()
    else :
        s3=s3+i.upper()
print(s3)
