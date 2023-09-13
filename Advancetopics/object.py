class Test:
    def __init__(self,a):
        self.var=a
        print("in constructor :",self.var)

obj=Test(10)
print("the value of a:",obj.var)
'''
print("the value of a:",obj.a)
AttributeError: 'Test' object has no attribute 'a'
'''
