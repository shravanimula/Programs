a=[]
n=int(input('enter the size of the list:'))
print("enter the list elements:")
for i in range(0,n):
    ele=int(input())
    a.append(ele)
print("the list elements are:")
print(a)

b=[]
n=int(input('enter the size of the list:'))
print("enter the list elements:")
for i in range(0,n):
    ele=int(input())
    b.append(ele)
print("the list elements are:")
print(b)

a.extend(b)
print(a)


c=[]
c.extend(a)
print(c)

