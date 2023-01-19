n = int(input("Unesite broj:   "))
if n%2 == 0:
    print("Broj je paran!")
n = int(input("Unesite broj:  "))
umnoz = 1
if n%2 !=0:
  while n!=0:
    z=n%10     # zadnja znamenka
    umnoz=umnoz*z # umnozak zadnje znamenke i prethodne
    n=n//10  # brisanje znamenke
print(umnoz)





