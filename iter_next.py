class Number:
    def __iter__(self):
        self.a=10
        return self
    
    def __next__(self):
        z=self.a
        self.a=self.a+1
        return z
    
obj=Number()
myiter=iter(obj)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
