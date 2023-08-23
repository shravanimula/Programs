#using remove method to delete one element in list
l=[1,2,3,4,5]
l.remove(4)
print(l)

l1=[]
n=int(input('enter the size of the list:'))
print("enter the list elements:")
for i in range(0,n):
    ele=int(input())
    l1.append(ele)
print("the list elements are:")
print(l1)

num=int(input('enter the number to remove:'))
l1.remove(num)
print(l1)


n2=int(input("enter the index to pop:"))
l1.pop(n2)
print(l1)

l1.pop()
print(l1)

l1.clear()
print(l1)
