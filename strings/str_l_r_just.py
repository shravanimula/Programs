s=input("enter a string:")
print(s.ljust(10,'#'))

s1=input("enter a string:")
n=int(input("enter a number:"))
replace=input("enter astring to fill :")
print(s1.ljust(n,replace))

print(s1)
s2=''
for i in s1:
    if i.islower():
        s2=s2+i.swapcase()

print(s2)


st=input("enter a string:")
print(st.rjust(15,'&'))

st1=input("enter a string:")
a=int(input("enter a number:"))
replace=input("enter astring to fill :")
print(st1.rjust(a,replace))

print(st1)
st2=''
for i in st1:
    if i.isalpha():
        st2=st2+i.upper()

print(st2)

