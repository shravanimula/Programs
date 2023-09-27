import re
targetstring=input("enter a target string")
replacement=input("enter the replacement string")
result=re.sub("hello",replacement,targetstring)
print(result)
