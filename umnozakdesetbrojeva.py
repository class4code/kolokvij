umn=1  # varijabla za umnozak jednaka 1
sp=0   # suma parnih
sn=0   #suma neparnih 
for i in range (10):
    broj=int(input("Unesite broj: "))
    umn=umn*broj
    if broj%2==0:  # ako je broj paran
        sp=sp+broj
    else:          # ako je broj neparan
        sn=sn+broj
print(umn, sp, sn)