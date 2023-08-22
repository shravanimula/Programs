word=input()
length=0
for i in word:
    length=length+1
#convert upper to lower and lower to upper

str1=""
for i in range(length):
    str1=str1+word[i].swapcase()

print("converting the upper to lower and lower to upper:",str1)
