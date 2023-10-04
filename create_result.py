print("CREATE RESULT")
print("------------------------------------------------------")
print("ENTER MARKS OUT OF HUNDRED")
a =int(input("Marks for mathes: "))
b =int(input("Marks for evs: "))
c =int(input("Marks for science: "))
d =int(input("Marks for ss: "))
e =int(input("Marks for hindi: "))
f =int(input("Marks for gujarati: "))

g=0

g+=a
g+=b
g+=c
g+=d
g+=e
g+=f

print("total marks: ",g)
print("------------------------------------------------------")

p=g*100/600
print("total percentage: ",p)
print("------------------------------------------------------")

if p<=33:
    print("grade: F")
elif p>33 and p<=45:
    print("grade: D")
elif p>45 and p<=60:
    print("grade: C")
elif p>60 and p<=75:
    print("grade: B")
elif p>75 and p<=85:
    print("grade: A")
else:
    print("grade: A+")

print("------------------------------------------------------")

if p>=75:
    print("Result: Distinction")
elif p<75 and p>=65:
    print("Result: First class")
elif p<65 and p>=50:
    print("Result: Second class")
elif p<50 and p>=33:
    print("Result: Pass class")
else:
    print("Result: Fail")







    
