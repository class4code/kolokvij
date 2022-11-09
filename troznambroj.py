while True:
    n = int(input("Unesite broj:  "))
    if n<1000 and n>99:
        print("Unesli ste troznam. broj!")
        break  # break point, prekid programa
    else:      # ako nije unešen troz. broj program nastavlja dalje sa radom
        print("Pokušajte ponovno!")