suma = 0
n = int(input("Koliko ima brojeva:  "))
for i in range(n):
    broj = eval(input("Unesi broj:  "))
    suma = suma + broj
p = suma/n
print("Prosjek: ", p)