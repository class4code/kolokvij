while 1:
 n = int(input("Unesi broj: "))
 if n>0:
   break

s=0
kopija = n
if kopija%2==0:
    while kopija !=0:
        znamenka = kopija%10
        s = s + znamenka
        kopija = kopija // 10
    print("Broj",n, "je paran. Suma znamnenki mu je ", s)
else:
    print("Broj nije paran:  ")



