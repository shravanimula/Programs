a=[]
n=int(input('enter the size of the list:'))
print("enter the list elements:")
for i in range(0,n):
    element=int(input())
    a.append(element)
            

print("the list elements are:")
print(a)

'sort the list'
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i] > a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp

print("after sort the list is :",a)
