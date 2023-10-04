print("LIST COMMON/UNCOMMON")

#common / uncommon

a = ["KOMAL","Het","Patel","ISS"]
b = ["por","KOMAL","Python","Patel"]

print(*a)
print(*b)

print(set(a).intersection(set(b)))

c = []
for i in a:
    if i not in b:
        c.append(i)
for i in b:
    if i not in a:
        c.append(i)

print(c)


print("-------------------------------------------------------------")


x = set(a).intersection(set(b))

print(set(a+b)- x)
