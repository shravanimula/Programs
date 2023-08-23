l=[]
n=int(input('enter the size of the list:'))
print("enter the list elements:")
for i in range(0,n):
    ele=int(input())
    l.append(ele)

print("befoore reverse the list:")
print(l)

l.reverse()
print("after reverse the list:")
print(l)

l1=l[::-1]
print("after reverseing the list l:")
print(l1)


l2=[1,2,3,4,5,6,7,8]
print("before reverse the list is:")
print(l2)
rev_list=[]
for i in l2:
    rev_list=[i]+rev_list

print("after reverese the list is:")
print(rev_list)

l3=[11,22,33,44,55,66]
print("before reverse:")
print(l3)
reverse_list=[]
for i in range(len(l3)):
    reverse_list.append(l3.pop())

print("after l3 reverse:")
print(reverse_list)
