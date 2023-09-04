#a{m,n}:minimum  m number of a's  and maximum n number of a's

import re
match=re.finditer("a{2,4}","abaacaaadaaaabaaaaa")
for a in match:
    print(a.start(),"...",a.end(),"...",a.group())

