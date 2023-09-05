class Student():
    def userinput(self):
        self.id=int(input("enter the student id:"))
        self.name=input("enter the student name:")
        self.marks=int(input("enter the student marks:"))
    def display(self):
        print("student id is:",self.id)
        print("student name is:",self.name)
        print("student marks is:",self.marks)

st1=Student()
st1.userinput()
st1.display()
