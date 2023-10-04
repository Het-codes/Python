print("CLASS OUTPUT")

from class_code import code

obj = code

#factorial
a = int(input("Find Factorial of : "))
print("Factorial of",a,"is",obj.loop1(a))

print("----------------------------------------------------------")

#pattern
b = int(input("Enter no. of rows and columns : "))
obj.loop2(b)

print("----------------------------------------------------------")

#age
c = int(input("Enter your birth year : "))
print("your age is",obj.age(c))

print("----------------------------------------------------------")

#area of circle
d = int(input("Enter radius : "))
print("Area of circle is",obj.area(d))

print("----------------------------------------------------------")

#all operation
x = input("Enter first value : ")
y = input("Enter second value : ")
z = input("Enter operation : ")
print("Your answer is",obj.all(x,y,z))

#loop  (IMP)
e = int(input("Enter start point : "))
f = int(input("Enter end point : "))
print(obj.loop3(e,f))











