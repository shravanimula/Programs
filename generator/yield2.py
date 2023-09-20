def fun():
    a=1
    b=2
    yield a+b
    a=11
    b=22
    yield a+b

result=fun()
print(next(result))
print(next(result))
