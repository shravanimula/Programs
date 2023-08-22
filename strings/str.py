#convert  list into string
a=['aaaa','bbbb','cccc','ddddd']
print(a)
s=' '
s=' '.join(a)
print(s)

string=' '
for i in a:
    string+=' '+i
print(string)


#convert the tuple into string
b=('aa','bb','cc','dd')
print(b)
b1=' '.join(b)
print(b1)
print(type(b1))
