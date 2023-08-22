s="abcd hello hih ok"
result=s.endswith('ok')
print(result)
re=s.endswith('hih')
print(re)

st="hello hii helo abcd he lo"
l=st.split()
a=[]
for i in l:
    if i.endswith('lo'):
        a.append(i)

print(a)

s1=' '.join(a)
print(s1)
