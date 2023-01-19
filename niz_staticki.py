while True:
    n = int(input("Koliko ima brojeva:  "))
    if n > 0:
        break
a = [0] * n

for i in range(n):
    a[i] = int(input("Unesi element niza: "))
print(a)    
