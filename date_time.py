print("DATE TIME")

import datetime

x = datetime.datetime.now()
print(x)

print("-----------------------------------------------------------------")

print(x.year,end='-')
print(x.month,end='-')
print(x.day)

print("-----------------------------------------------------------------")

print("Today's day is",x.strftime("%A"))

print("-----------------------------------------------------------------")

print("Date and time:",x.strftime("%Y-%m-%d %H:%M:%S"))

print("Date:",x.strftime("%Y-%m-%d"))
