import re
n=input("Enter mobile number:")
m=re.fullmatch("[6-9]\d{9}",n)
if m!= None:
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
