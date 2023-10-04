print("DIGIT SUM")

a = input("Enter value: ")

if a == "":
    a = input("Please enter a value: ")

b = len(a)
sum = 0

for i in range(0,b):
    sum = sum + int(a[i])
print("Digit sum is: ",sum)


print("----------------------------------------------------------------")

total = 0
for j in a:
    total = total+int(j)
print(total)
