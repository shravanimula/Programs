t=(1,2,3,4,5,6)
print(t)
l=list(t)
rev=[]
for i in l:
    rev=[i]+rev

t=tuple(rev)
print("reverse of the tuple is:")
print(t)


a=(1,2,3,4,5)
print(a)
l1=list(a)
l1.reverse()
a=tuple(l1)
print(a)
