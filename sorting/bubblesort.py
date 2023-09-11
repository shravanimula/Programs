def bubble_sort(a,size):
    for i in range(size):
        for j in range(0,size-i-1):
            if a[j] > a[j+1]:
                a[j] , a[j+1] = a[j+1] ,a[j]
                
    print("\n after sorting the array is:")
    for i in range(size):
        print(a[i],end=" ")


array=[]
n=int(input("enter the size of array"))
for i in range(n):
    ele=int(input())
    array.append(ele)

print("before sorting the array is:")
for i in range(len(array)):
    print(array[i],end=" ")

bubble_sort(array,n)
