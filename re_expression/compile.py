import re
count=0
pattern=re.compile("hi")
match=pattern.finditer("hihellohihaahi")
for m in match:
    count+=1
    print(m.start(),"...",m.end(),"...",m.group())

print("The number of occurrences: ",count)
