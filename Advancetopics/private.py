'''
class A:
    __a=10  #private variable

class B:
    def fun():
        print("a value is:",A.__a)
    #AttributeError: type object 'A' has no attribute '_B__a'. Did you mean: '_A__a'?
B.fun()

'''

