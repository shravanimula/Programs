import re
a=input("enter the string to check:")
b=re.search("hello",a)
if b!=None:
    print("match is available and the first occurance is")
    print("Start Index:",b.start(), "and End index:",b.end())
else:
    print("match is not available in the string")

print(b) 
