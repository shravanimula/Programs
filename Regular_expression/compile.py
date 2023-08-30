#compile () : This function is used to compile a pattern into Regex Object.
#finditer(): Returns an Iterator object which , Match object for every Match

#match object can call the start ,end and group
#start() : Returns start index of the match
# end() : Returns end+1 index of the match
#  group() : Returns the matched string



import re
count=0
pattern=re.compile("ab")
match=pattern.finditer("abaababa")
for m in match:
    count+=1
    print(m.start(),"...",m.end(),"...",m.group())
    print("The number of occurrences: ",count)



'''ouput :
0 ... 2 ... ab
The number of occurrences:  1
3 ... 5 ... ab
The number of occurrences:  2
5 ... 7 ... ab
The number of occurrences:  3
'''
