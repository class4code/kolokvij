radniDani = ["PON","UTO","SRI","ČET","PET"]
br=0
while True:
        unos = input("Unesite dan u tjednu:  ") 
        if unos not in radniDani:
                break      
        if unos in radniDani:
           print(unos,br)
           br=br+1

        
 