x = int(input("Unesi broj:  "))
suma=0  # sumu postavimo na 0
br=0 # brojač
for i in range (1,x+1): # za svaki x od 1 do x+1 ponavljaj
    if suma<x: # za svaki broj manji od x 
        suma=suma+i # zbroji prethodnu vrijednost
        print(suma) # ispiši sumu
        br=br+1     # povećaj brojač za 1        
print("Zbrojeno je ", br , "brojeva")
