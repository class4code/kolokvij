def Prost(broj):
    for i in range(2,broj):
        if broj % i == 0:
            return False
    return True

while True:
    broj = int(input('Unesite broj veći od 100:  '))
    if broj > 100:
        break

prostiFaktori = str(broj) + "="
while not(Prost(broj)):
    for i in range(2,broj):
        if Prost(i) and broj % i == 0:
            prostiFaktori += str(i) + " * "
            broj = broj // i
            break

prostiFaktori += str(broj)

print(prostiFaktori)

