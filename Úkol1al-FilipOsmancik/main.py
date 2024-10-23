#Generuje náhodné čísla
import random

#Prázdné pole
area = []

#9 náhodných čísel (0-100)
for _ in range(9):
    cislo = random.randint(0, 100)
    area.append(cislo)

#Vypsání pole
print("Area:", area)

#Tímto jsem dostal první, prostřední a poslední hodnotu pole
prvni_hodnota = area[0]
prostredni_hodnota = area[4]
posledni_hodnota = area[8]

#Zde se vypíše první, prostřední a poslední hodnota
print("Prvni hodnota:", prvni_hodnota)
print("Prostredni hodnota:", prostredni_hodnota)
print("Posledni hodnota:", posledni_hodnota)

#Zaměnění 5. indexové hodnoty pole (area) za číslo 34
area[4] = 34
#Vypsání pole (area)
print("Pole (area) po zaměnění 5. indexové hodnoty za 34:", area)

#Vypsání indexově 7 hodnoty z pole
print("7. hodnota:", area[6])

#Vypsání délky pole
print("Pole (area) je dlouhé:", len(area))

#Vypsání minimální a maximální hodnoty pole
print("Minimální hodnota v poli:", min(area))
print("Maximální hodnota v poli:", max(area))

#Vytvoření druhého pole s libovolnými čísly a libovolnou délkou
area_2 = [17, 18, 21, 66, 69]

#Zde se vypíše druhé pole v mém případě (area_2)
print("Druhé pole", area_2)

#Sečtení obou polí a vypsání
secteni_poli = area + area_2
#Vypsání obou polí
print("Obě pole:", secteni_poli)

#Sečtení 1 a 5 hodnoty z pole č.2. (indexově)
secteni_hodnot = area_2[1] + area_2[5]
#Vypsání celkového výsledku
print("Celkový výsledek je:", secteni_hodnot)
