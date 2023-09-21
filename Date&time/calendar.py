import calendar
cal=calendar.month(2023,9)
print(cal)

a=calendar.isleap(2020)
print(a)

b=calendar._prevmonth(2023,9)
print(b)
print(type(b))

c=calendar._nextmonth(2023,9)
print(c)
