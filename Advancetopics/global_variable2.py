a=10
class Test:
    def func(a):
    #   global a   #SyntaxError: name 'a' is parameter and global
        a=a+20
        print(a)

Test.func(20)
print(a)
