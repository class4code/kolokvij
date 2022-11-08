password = "  "   # varijabla u koju ćemo spremati string, pogađati lozinku
while password !="tajno": # sve dok je password različito od tajno, ponavljaj
    password = input("Unesite lozinku: ") # traži unos lozinke
    if password == "tajno": # uspoređujemo unešenu lozinku sa tajno
      print("Upisali ste točnu lozinku: ")        
    else:
      print("Upisali ste pogrešnu lozinku, pokušajte ponovno")