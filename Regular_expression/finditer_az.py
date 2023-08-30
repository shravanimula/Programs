import re
match=re.finditer("[a-z]","a7Sb@k9#Az")
for a in match:
    print(a.start(),"...",a.end(),"...",a.group())

