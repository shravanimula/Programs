#a{m,n} is minimum m number of a's and maximum n number a's
import re
count=0
match=re.finditer("h{2,3}","hellohhihhahhh")
for m in match:
    count=count+1
    print(m.start(),"....",m.end(),"....",m.group())
print("count the occurence",count)
