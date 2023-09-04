import re
a=re.subn("[0-9]","*",'1ab2c3d4e5')
print(a)
print(a[0])
print("the number of replacement:",a[1])
