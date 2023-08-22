#print the count of substring in the main string

s="str is in is main is string"
substr="is"
c=s.count(substr)
print("count of substring is:",c)

#using for and if loops 
s=s.split()
count=0
print(s)
for i in s:
    if i == substr:
        count=count+1

print("count of substr is:",count)


#user input 
st=input("enter a string")
substr1=input("enter a substring:")
st=st.split()
cnt=0
for word in st:
    if word == substr1:
        cnt+=1

print("count of substr is :",cnt)
