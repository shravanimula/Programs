class Student:
    def __init__(self,a,b,c):
        self.id=a
        self.name=b
        self.marks=c

    def display(self):
        print("student id:",self.id)
        print("student name:",self.name)
        print("student marks:",self.marks)

st1=Student(1,"aaaa",11)
st2=Student(2,"bbbbb",22)
st1.display()
st2.display()
