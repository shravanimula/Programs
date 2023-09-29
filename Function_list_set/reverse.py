a=[1,2,3,4,5,6,7]
print("before reverse the list elements are:", a)
b=a[::-1]
print("after reverse: ",b)
rev_list=[]
for i in a:
    rev_list=[i]+rev_list
print("reverse list:",rev_list)


