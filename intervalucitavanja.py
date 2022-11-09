jz=0  # varijabla brojača za jednoznamenkaste
dz=0  # varijabla brojača za dvoznamenkaste
tz=0  # varijabla brojača za troznamenkaste
for i in range (1,1000):
    x=int(input("Unesi broj:  "))
    if x == 0:  # ako se unese nula program se prekida 
       break
    if x<10:     # za sve brojeve manje od 10 
        jz=jz+1   # povećaj brojač za 1
    if x>=10 and x <100:
        dz = dz + 1
    if x >=100 and x <1000:
        tz = tz + 1
print("Broj jednoznamenkastih je: ", jz)
print("Broj dvoznamenkastih je: ",   dz)
print("Broj troznamenkastih je: ",   tz)