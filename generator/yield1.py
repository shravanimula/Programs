def fun(n):
    while n > 0:
        yield n
        n=n-1


for i in fun(10):
    print(i)
