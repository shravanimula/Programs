class Student:
    def __init__(self):
        self.id=111
        self.name="aaa"
        self.marks=11.1
    def display(self):
        print("student id is:",self.id)
        print("student name is:",self.name)
        print("student marks is:",self.marks)

st1=Student()
st1.display()
