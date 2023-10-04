print("CREATE CALANDER")

a = int(input("Enter value: "))

for i in range(1,a+1):
    print(str(i).zfill(2),end=" ")
    if i%7==0:
        print("\n")
    
