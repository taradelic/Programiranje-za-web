import random

def main():
    trazeni_broj = random.randint(1,10)

while True:
    try:
        unos = int(input("Pokušajte pogoditi broj od 1 do 10:"))

    if unos == trazeni_broj:
        print("Bravo, pogodili ste traženi broj!")
        break
    else:
        print(f"Netočno traženi broj je bio {trazeni_broj}. Pokušajte ponovo.")
    except ValueError:
    print("Unesi valjani broj od 1 do 10")

