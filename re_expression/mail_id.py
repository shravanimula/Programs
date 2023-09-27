import re
mailid=input("enter the mailid:")
a=re.fullmatch("\w[a-zA-z0-9.]*@gmail[.]com",mailid)
if a!=None:
    print("vaild mail id")
else:
    print("invalid mail id")
