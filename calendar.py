import calendar
a=int(input("enter year:"))
b=int(input("enter month:"))

m=calendar.calendar(a)
print(m)

m=calendar.month(a,b)
print(m)

from datetime import date
a=date(2005,12,14)
b=date(2026,4,28)
print("no.of days she lived: ",(b-a).total_seconds()/3600)

