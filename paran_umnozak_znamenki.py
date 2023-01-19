while 1:
  n=int(input("Unesi cijeli broj:  "))
  if n>0:
    break

umnozak=1
kopija=n
if kopija%2 !=0:
    while kopija>0:
        znamenka = kopija%10
        umnozak = umnozak * znamenka
        kopija = kopija//10
print("Broj ", n , " je neparan. Umnozak znamenki mu je" ,  umnozak)

