print("MATRIX WITH LOOP + LIST")

a = [["KOMAL","ISS","PATEL"],["HET","PATEL","PYTHON"],["LDCE","EC","POR"]]

b = len(a)

for i in range(0,b):
    for j in range(0,len(a[i])):
        print(a[j][i],end=" ")
    print("")
