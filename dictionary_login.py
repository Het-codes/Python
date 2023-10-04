print("LOGIN")

a = input("Enter username: ")
b = input("Enter passward: ")
c = input("Enter username: ")
d = input("Enter passward: ")


login={"het":{"username":a,"password":b},"raj":{"username":c,"passward":d}}

print(login)

print("------------------------------------------------------------------")

x = input("Enter username: ")
y = input("Enter passward: ")

for i in login:
    for j in i:
        if x==login[i]["username"] and y==login[i]["password"]:
            print("true")
            break
        else:
            print("Invalid")
            break

