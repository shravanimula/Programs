'''
We can use match function to check the given pattern at beginning of
target string.
If the match is available then we will get Match object, otherwise we
will get None.
'''
import re
a=input("enter the string to check:")
b=re.match("hello",a)
if b!=None:
    print("match is available at the beginning of the String")
    print("Start Index:",b.start(), "and End index:",b.end())
else:
    print("match is not available in the string")

print(b)
