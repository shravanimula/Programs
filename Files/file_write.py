fp=open("demo.txt","w")
fp.write("hello this is new python file")
fp.close()

f=open("demo1.txt","w")
f.write("new file in python")
f.close()

fp=open("demo.txt","a")
fp.write("adding new line the demo file")
fp.close()

fp=open("demo.txt","r")
print(fp.read())
fp.close()

fp1=open("demo2.txt","w+")
fp1.write("this is demo2 file")
fp1.seek(0)
word=fp1.read()
print(word)
fp1.close()

fp=open("demo2.txt","r+")
print(fp.read())
fp.write("adding new line to the demo2 file")
fp.seek(0)
print(fp.read())
fp.close()
