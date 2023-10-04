print("CREATE BOOKING DATE")

import datetime

b = int(input("Enter days: "))
x = datetime.datetime.now()
y = x + datetime.timedelta(days=b)
z = x.strftime('%d-%m-%y')
c = y.strftime('%d-%m-%y')

print("Your tour start on: ",z)
print("Your tour ends on: ",c)

