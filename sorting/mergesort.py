def mergesort(a):
    if len(a) > 1:
        mid=len(a) // 2
        left=a[:mid]
        right=a[mid:]
        mergesort(left)
        mergesort(right)
        i=j=k=0
        while i<len(left) and j<len(right): 
            if left[i] <= right[j]:
                a[k]=left[i]
                i=i+1
            else:
                a[k]=right[j]
                j=j+1
            k=k+1

#checking any element was left
        while i<len(left):
            a[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
            a[k]=right[j]
            j=j+1
            k=k+1

def display(a):
    for i in range(len(a)):
        print(a[i] ,end=' ')

array=[]
size=int(input("enter the size of array:"))
print("enter the array elements are:")
for i in range(size):
    ele=int(input())
    array.append(ele)

print("before sorting the array elements are:")
display(array)

mergesort(array)

print("\nafter sorting the array is:")
display(array)

