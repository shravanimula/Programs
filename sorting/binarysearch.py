def binarysearch(a,left,right,ele):
    while left <=right:
        mid=left+(right-left)//2
        if a[mid] == ele:
            return mid
        elif a[mid] < ele:
            left=mid+1
        else:
            right=mid-1
    return -1


array=[]
size=int(input("enter the size of the array:"))
print("enter the array elements are:")
for i in range(size):
    ele=int(input())
    array.append(ele)

print("the array elements are:")
for i in range(size):
    print(array[i],end=" ")

element=int(input("\nenter the  element to search:"))
result=binarysearch(array,0,len(array)-1,element)
if result == -1:
    print("element is not present in the array")
else:
    print("element is present in the array:",result)
