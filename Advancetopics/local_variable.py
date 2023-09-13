class Name:
    a=10
    def fun(a):
        print(a)
        Name.a=Name.a+a

Name.fun(100)
print(Name.a)
