#we can use quantifiers to specify the number of occurrences to match

import re
match=re.finditer("a","abaacaaadaaaabaaaaa")
for a in match:
    print(a.start(),"...",a.end(),"...",a.group())
