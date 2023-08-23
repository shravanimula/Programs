l=[1,2,3,4,5,6,7]
print(len(l))

length=0
for i in l:
    length+=1

print("length of the string:",length)

l1=[]
n=int(input('enter the size of the list:'))
print("enter the list elements:")
for i in range(0,n):
    ele=int(input())
    l1.append(ele)
print("the list elements are:")
print(l1)
length1=0

for i in l1:
    length1+=1

print("length of l1 is:",length1)

