def fun():
    yield 11
    yield "aaa"
    yield 23.9

for i in fun():
    print(i)
