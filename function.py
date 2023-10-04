"""print("FUNCTIONS")

def loop1(a):
    f = 1
    for k in range(1,a+1):
        f = f * k
    return f

def loop2(b):
    for i in range(0,b+1):
        print(" "*(b-i) + "*"*i)

def age(c):
    import datetime

    j = datetime.datetime.now()

    print("Your age is",j.year-c)

def area(d):
    d*=d
    e=3.14*d
    print("Area of circle is",e)

def all(x,y,z):
    ans1 = 0
    ans1 = eval(x+z+y)
    ans2 = str(ans1)
    eval(ans2)
    print("Your answer is",ans2)

#factorial
a = int(input("Find Factorial of : "))
print("factorial of",a,"is",loop1(a))

print("----------------------------------------------------------")

#pattern
b = int(input("Enter no. of rows and columns : "))
loop2(b)

print("----------------------------------------------------------")

#age
c = int(input("Enter your birth year : "))
age(c)

print("----------------------------------------------------------")

#area of circle
d = int(input("Enter radius : "))
area(d)

print("----------------------------------------------------------")

#all operation
x = input("Enter first value : ")
y = input("Enter second value : ")
z = input("Enter operation : ")
all(x,y,z)"""

i=0
def sum(a,i):
    while i< len(a)-2:
        a[i+2] = (a[i]+a[i+1])*a[i+2]
    
        sum(a,i+2)
        if i>= len(a)-2:
            x = a[i+2]
            return x

a = [1,2,3,4,5,6,7]
y = sum(a,i)
print(y)










