import re
match=re.finditer("[abc]","a7Sb@k9#Az")
for a in match:
    print(a.start(),"...",a.end(),"...",a.group())

match=re.finditer("[^abc]","a7Sb@k9#Az")
for b in match:
    print(b.start(),"...",b.end(),"...",b.group())

