print("REVERSE LOOP")

a = int(input("Enter starting point: "))
b = int(input("Enter ending point: "))
c = int(input("Enter decriment value: "))

for i in range(b,a-1,-c):
    print(i)
