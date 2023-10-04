print("CALANDER USING LIST")

a = ["MO","TU","WE","TH","FR","SA","SU"]

b = int(input("Enter Month Days: "))

c = input("Enter starting Day: ")


print("\n")

print(*a)

e = a.index(c)

#print(e)

w = len(a)

#print(w)
d = e
day = 1
for i in range(1,b+1+d):

    if(d+1) > i:
        print(str("  "), end=" ")
        #print(i)
    elif i%w==0:
        print(str(day).zfill(2),end="\n")
        day+=1
    else:
        print(str(day).zfill(2),end=" ")
        day+=1
''' else:
        
        print(str(day).zfill(2),end=" ")
        day+=1
        
        
    if i%w==0:
        print(str(day).zfill(2),"\n")
        day+=1'''
        

'''d = 0

if b == "":
    d=1
elif c == "MO":
    d=1
elif c == "TU":
    d=2
elif c == "WE":
    d=3
elif c == "TH":
    d=4
elif c == "FR":
    d=5
elif c == "SA":
    d=6
elif c == "SU":
    d=7
else:
    print("Day not valid")

for k in a:
    print(k,end=" ")
    
print("\n")

for i in range(0,d+1):
     print("  ",end="")
    
for j in range(1,b+1):
    print(str(j).zfill(2),end=" ")
    if (d+j-1)%7==0:
        print("\n")'''




















