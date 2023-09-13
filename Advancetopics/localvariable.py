class Test:
    n=10
    
    def func():
        n=20
        print("local n:",n)
        print("class variable n:",Test.n)

Test.func()
print("outside class :",Test.n)
#print(n)  NameError: name 'n' is not defined
