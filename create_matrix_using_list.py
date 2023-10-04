print("MATRIX USING LIST")
print("\n")

print("Enter 9 values: ",end="")

a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())
a6 = int(input())
a7 = int(input())
a8 = int(input())
a9 = int(input())
print("\n")

a = [a1,a2,a3,a4,a5,a6,a7,a8,a9]
b = 0
j = 0
c = len(a)
for i in range(1,c+1):
    if i%3==0:
        b+=a[j]
        print(a[j],end="\n")
        j+=1
    else:
        b+=a[j]
        print(a[j],end=" ")
        j+=1
    
print("\n")
print("---------------------------------------------------------------------------")
print("Total: ",b)
