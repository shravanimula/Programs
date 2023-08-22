word=input()
#convert some specific position to upper
length=0
for i in word:
    length=length+1

print("length of the string is:",length)
string=""
for i in range(length):
    if i%2==0:
        string+=word[i].upper()
    else:
        string+=word[i].lower()
print(string)

