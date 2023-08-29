fp=open("file.txt","a")
fp.write("iam adding new line to the file")
fp.close()

f=open("file.txt","r")
print(f.read())
f.close()
