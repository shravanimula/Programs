import re
a="hello world,hello good morning india 25"
b=re.findall("hello",a)
print(b)

c="hello world,hello good morning india 25"
d=re.findall("z",c)
print(d)
