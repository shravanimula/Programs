class Num:
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        if self.a <=15:
            b=self.a
            self.a=self.a+1
            return b
        else:
            raise StopIteration


obj=Num()
myiter=iter(obj)

for i in myiter:
    print(i)
