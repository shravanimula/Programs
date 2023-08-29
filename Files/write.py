fp=open("text2.txt","w")
fp.write("hello python")
fp.write("this is file operations")
fp.close()

fp=open("text2.txt","r")
for lines in fp:
    print(lines)
