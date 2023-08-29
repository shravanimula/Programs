#split function splits the variables when space is encountered

with open("text1.txt","r") as fp:
    lines=fp.readlines()
    for word in lines:
        element=word.split()
        print(element)
