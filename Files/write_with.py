#using with we can write the statements
with open("file.txt","w") as fp:
    fp.write("hello world")

with open("file.txt","r") as fp:
    data=fp.read()
print(data)
