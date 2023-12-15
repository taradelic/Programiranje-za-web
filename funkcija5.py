def izracunajKorake(put, korak):
    return int(put / korak)

put= float(input("Unesi duljinu puta (u metrima): "))
korak= float(input("Unesi duljinu koraka (u metrima): "))

print(izracunajKorake(put, korak))