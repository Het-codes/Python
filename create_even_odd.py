print("CREATE EVEN/ODD NUMBERS")

a = int(input("Enter value: "))

for i in range(1,a+1,2):
    print("Odd: ",i)

for j in range(0,a+1,2):
    print("Even: ",j)


'''new
c=[]
b=[]
for x in range(0,a+1):
    if x%2==0:
        c.append(x)
    else:
        b.append(x)
print(c)
print(b)
'''
