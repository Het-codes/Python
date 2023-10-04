
class code:
#factorial
    def loop1(a):
        f = 1
        for k in range(1,a+1):
            f = f * k
        return f

#pattern
    def loop2(b):
        for i in range(0,b+1):
            print(" "*(b-i) + "*"*i)

#age
    def age(c):
        import datetime

        j = datetime.datetime.now()
        age = j.year-c
        return age

#area of circle    
    def area(d):
        d*=d
        e=3.14*d
        return e

#all operations
    def all(x,y,z):
        ans1 = 0
        ans1 = eval(x+z+y)
        ans2 = str(ans1)
        eval(ans2)
        return ans2

#loop  (IMP)
    def loop3(a,b):
        j = []
        for i in range(a,b+1):
            j.append(i)
        return j 













