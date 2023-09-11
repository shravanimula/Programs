def selectionsort(a,n):
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if a[min] > a[j]:
                min=j

        a[i] , a[min]=a[min] ,a[i]

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

selectionsort(array,size)
