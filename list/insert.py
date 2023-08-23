a=[]
n=int(input('enter the size of the list:'))
print("enter the list elements:")
for i in range(0,n):
    ele=int(input())
    a.append(ele)
print("the list elements are:")
print(a)

a.insert(4,44)
print(a)
num=int(input("enter number:"))
pos=int(input("enter the position"))
a.insert(pos,num)
print(a)

