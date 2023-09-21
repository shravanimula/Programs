#We can convert date object to a string representation using two functions isoformat() and strftime().
from datetime import datetime
obj=datetime.now()
t=obj.strftime("%H:%M:%S")
print("time:",t)

DT=obj.strftime("%m-%d-%y, %H:%M:%S")
print("date and time is:",DT)

today=datetime.today()
str=datetime.isoformat(today)
print(str)
