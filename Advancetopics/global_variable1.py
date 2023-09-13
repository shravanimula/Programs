#can access the global variable inside the function using global  keywords
a=10
class A:
    a=20
    def fun():
        global a
        print("global a:",a)
        a=a+30  #modify the gloabl varaible 
        print(A.a)

A.fun()
print("global of a:",a)
print("class variable of a is:",A.a)
