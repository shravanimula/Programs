with open("file.txt","r") as fp:
    print(fp.tell())
    print(fp.read(8))
    print(fp.tell())
    print(fp.seek(3))
    print(fp.read(4))
    print(fp.tell())
