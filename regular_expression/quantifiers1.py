#a+:at least one a
import re
match=re.finditer("a+","abaacaaadaaaabaaaaa")
for a in match:
    print(a.start(),"...",a.end(),"...",a.group())

