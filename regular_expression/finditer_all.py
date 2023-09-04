import re
match=re.finditer("[0-9]","a7Sb@k9#Az")
print("it will print only numbers")
for a in match:
    print(a.start(),"...",a.end(),"...",a.group())


match=re.finditer("[a-zA-Z]","a7Sb@k9#Az")
print("it will print characters")
for b in match:
    print(b.start(),"...",b.end(),"...",b.group())


match=re.finditer("[a-zA-Z0-9]","a7Sb@k9#Az")
print("it print all except special characters")
for c in match:
    print(c.start(),"...",c.end(),"...",c.group())



match=re.finditer("[^a-zA-Z0-9]","a7Sb@k9#Az")
print("it print only special characters")
for d in match:
    print(d.start(),"...",d.end(),"...",d.group())
