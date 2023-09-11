def insertionsort(a,n):
    for i in range(1,n):
        temp=a[i]
        j=i-1
        while (j>= 0 and a[j] > temp):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=temp
    print("\nafter sorting the array is:")
    for i in range(n):
        print(a[i],end=' ')
array=[]
size=int(input("enter the size of array:"))
print("enter the array elements are:")
for i in range(size):
    ele=int(input())
    array.append(ele)

print("before sorting the array elements are:")
for i in range(size):
    print(array[i],end=' ')

insertionsort(array,size)
