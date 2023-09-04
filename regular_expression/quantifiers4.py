#a{n}:exactly 'n' number of a's
import re
match=re.finditer("a{3}","abaacaaadaaaabaaaaa")
for a in match:
    print(a.start(),"...",a.end(),"...",a.group())
