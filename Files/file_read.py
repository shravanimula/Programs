'''
fp=open("demo1.txt","r") #FileNotFoundError
print(fp.read())# try to reading withput exist file
'''
fp=open("demo.txt","r")
print(fp.read())
fp.close()

fp=open("demo.txt","r")
print(fp.read(8))#try to read specific characters
fp.close()

fp=open("demo.txt","r")
print(fp.readline()) #it will read one line
print(fp.readline())
fp.close()

fp=open("demo.txt","r")
for i in fp:
    print(i)

fp.close()
