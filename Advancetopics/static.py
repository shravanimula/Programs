'''
We can access instance methods within the class by using self
 Ex: self.methodname ( )

We can access instance methods outside of the class by using object reference
Ex: objectreference.methodname( )
'''


#While declaring class methods we should pass class variable i.e. cls
# Using cls we can access class or static variables inside the class methods
# We can access class methods either by using class name or object reference



class Student:
    name="aaa"
    def __init__(self):
        print("inside the constructor")
        print(self.name)
        print(Student.name)

    def fun1(self):    #instance method
        print("inside the method")
        print(self.name)
        print(Student.name)

    def fun2(cls):      #class method
        print("inside class method")
        print(cls.name)
        print(Student.name)


details=Student()
details.fun1()
details.fun2()
print("outside the class")
print(Student.name)
print(details.name)

