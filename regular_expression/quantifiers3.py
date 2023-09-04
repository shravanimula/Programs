#a?:at most a i.e, either zero number or one number

import re
match=re.finditer("a?","abaacaaadaaaabaaaaa")
for a in match:
    print(a.start(),"...",a.end(),"...",a.group())
