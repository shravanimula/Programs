def fun():
    yield 11
    yield "aaa"
    yield 23.9

result=fun()
print(next(result))
print(next(result))
print(next(result))
