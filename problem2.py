# Funkcija za zbrajanje
def zbroj(a, b):
    return a + b

# Funkcija za oduzimanje
def razlika(a, b):
    return a - b

# Funkcija za množenje
def umnozak(a, b):
    return a * b

# Funkcija za dijeljenje
def kolicnik(a, b):
    if b == 0:
        return "Nije moguće dijeliti s nulom"
    else:
        return a / b

# Unos brojeva
broj1 = float(input("Unesite prvi broj: "))
broj2 = float(input("Unesite drugi broj: "))

# Odabir operacije
print("Odaberite matematičku operaciju:")
print("1. Zbrajanje (+)")
print("2. Oduzimanje (-)")
print("3. Množenje (*)")
print("4. Dijeljenje (/)")

odabir = input("Unesite broj operacije (1/2/3/4): ")

# Izvršavanje odabrane operacije i ispis rezultata
if odabir == "1":
    rezultat = zbroj(broj1, broj2)
    print(f"Zbroj {broj1} i {broj2} je {rezultat}")
elif odabir == "2":
    rezultat = razlika(broj1, broj2)
    print(f"Razlika {broj1} i {broj2} je {rezultat}")
elif odabir == "3":
    rezultat = umnozak(broj1, broj2)
    print(f"Umnožak {broj1} i {broj2} je {rezultat}")
elif odabir == "4":
    rezultat = kolicnik(broj1, broj2)
    print(f"Količnik {broj1} i {broj2} je {rezultat}")
else:
    print("Pogrešan unos operacije. Molimo unesite 1, 2, 3 ili 4.")
