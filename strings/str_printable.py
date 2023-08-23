st="hello hi\t"
print(st.isprintable())

s=input("enter a string:")
print(s.isprintable())

l=[]
for i in s:
    if i.isprintable():
        l.append(i)

print(l)

