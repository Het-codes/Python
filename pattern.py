print("PATTERN")

a = int(input("Enter Rows And Columns : "))

for i in range(0,a):
    for j in range(0,i+1):
        print("*",end="")
    print("")

print("--------------------------------------------------------")

for x in range(0,a+1):
    print(" "*(a-x) + "*"*x)
        
print("--------------------------------------------------------")

for i in range(a,0,-1):
    for j in range(0,i):
        print("*",end="")
    print("")
