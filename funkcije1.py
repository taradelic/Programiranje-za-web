# Funkcije
def zbroj (a,b):
    rezultat = a + b
    print( rezultat)

def oduzmi(a,b):
    rezultata = a - b
    print(rezultata)

def mnozi(a,b):
    rezultat = a * b
    print(rezultat)

def dijeli(a,b):
    rezultat = a / b
    print(rezultat)

#unos
a = int(input("Unesi broj a: "))
b = int(input("Unesi broj b: "))
o = input("Odaberi matematičku operaciju +, -, *, / ")

#odabir
if o == "+":
    zbroj(a,b)
elif o == "-":
    oduzmi(a,b)
elif o == "*":
    mnozi(a,b)
elif o == "/":
    dijeli(a,b)
    