#1. Vytvoř pole, které bude mít 5 stringových hodnot.
area = ["Pole1", "Pole2", "Pole3", "Pole4", "Pole5"]
print("Pole", area)
#2. Přidej pomocí metody append() jeden prvek. - "vítr".
area.append("vitr")
print("vitr2", area)
#3. Odstraň pomocí metody remove() druhý prvek z pole.
area.remove("Pole2")
print("Odstranění pomocí metody() druhý prvek z pole", area)
#4. Zaměň 5 hodnotu z pole za: "slunce".
area[4] = "Slunce"
print("Zaměnění 5 hodnoty z pole za slunce", area)
#5. Přidej 2 stringové hodnoty pole pomocí metody extend().
area.extend(["Pole6", "Pole7"])
print("Přidat Pole6 a Pole7", area)