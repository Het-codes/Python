print("CREATE TABLE")

a = int(input("Enter table no.: "))
b = int(input("Enter table position: "))

for i in range(1,b+1):
    #print(a,i,sep=" x ",end=" = ")
    #print(a*i)
    print(a,"x",i,"=",(a*i))
