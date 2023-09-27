#a{m} it exactly m number of a's

import re
count=0
match=re.finditer("h{2}","hellohihh")
for m in match:
    count=count+1
    print(m.start(),"....",m.end(),"....",m.group())
print("count the occurence",count)
