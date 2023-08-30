import re
match=re.finditer("\s","a7Sb @k 9#Az")
print("it print only space")
for a in match:
    print(a.start(),"...",a.end(),"...",a.group())

match=re.finditer("\S","a7Sb @k 9#Az")
print("it print except space")
for a in match:
    print(a.start(),"...",a.end(),"...",a.group())

match=re.finditer("\d","a7Sb @k 9#Az")
print("it print only digits:")
for a in match:
    print(a.start(),"...",a.end(),"...",a.group())

match=re.finditer("\D","a7Sb @k 9#Az")
print("it print except digit")
for a in match:
    print(a.start(),"...",a.end(),"...",a.group())

match=re.finditer("\w","a7Sb @k 9#Az")
print("it print any word character:")
for a in match:
    print(a.start(),"...",a.end(),"...",a.group())



match=re.finditer("\W","a7Sb @k 9#Az")
print("it print special character")
for a in match:
    print(a.start(),"...",a.end(),"...",a.group())


match=re.finditer(".","a7Sb @k 9#Az")
print("it will any character including spcecial characters:")
for a in match:
    print(a.start(),"...",a.end(),"...",a.group())
