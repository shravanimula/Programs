a=[]
n=int(input('enter the size of the list:'))
print("enter the list elements:")
for i in range(0,n):
    ele=int(input())
    a.append(ele)

print("the list elements are:")
print(a)
length=0
for i in a:
    length+=1

print("the length of the  list:",length)
