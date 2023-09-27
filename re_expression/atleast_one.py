import re
count=0
match=re.finditer("h+","hellohihh")
for m in match:
    count=count+1
    print(m.start(),"....",m.end(),"....",m.group())
print("count the occurence",count)
