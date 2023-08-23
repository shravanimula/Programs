#A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces
s=input("enter a string:")
print(s.isidentifier())

l=[]
for i in s:
    if i.isidentifier():
        l.append(i)

print(l)
