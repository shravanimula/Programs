#a*:any numbers of a's including zero numbers
import re
match=re.finditer("a*","abaacaaadaaaabaaaaa")
for a in match:
    print(a.start(),"...",a.end(),"...",a.group())

