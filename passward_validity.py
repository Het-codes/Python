print("PASSWORD VALIDITY")

a = input("Enter password: ")
b = 1

if len(a)<6 and len(a)>12:
    print('length should be between 6 and 12')

if not any(i.isdigit() for i in a):
    print("Used atleast 1 digit")
    b-1
elif not any(i.islower() for i in a):
    print("Used atleast 1 lower case")
    b-1
elif not any(i.isupper() for i in a):
    print("Used atleast 1 upper case")
    b-1
elif not any(i in ["@","#","$"] for i in a):
    print("Used atleast 1 upper case")
    b-1
else:
    print("valid password")
