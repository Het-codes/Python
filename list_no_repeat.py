print("LIST NO REPEAT VALUE")

#No Repeat Value

a = ["KOMAL","Het","Patel","ISS","Het","Patel"]

print(*a)

a = list(dict.fromkeys(a))
print(a)

print("------------------------------------------------")

#Ascending / Descending

b = ["por","komal","python","patel"]

print(*b)

b.sort()
print(b)

b.sort(reverse=True)
print(b)
