def kalkulacka():
    print("Vítejte v kalkulačce!")
    
    # Získání čísel od uživatele
    try:
        cislo1 = float(input("Zadejte první číslo: "))
        cislo2 = float(input("Zadejte druhé číslo: "))
    except ValueError:
        print("Chyba: Zadaná hodnota není číslo.")
        return

    # Získání operace od uživatele
    operace = input("Vyberte operaci (+, -, *, /): ")

     # Vykonání operace a výpočet
    if operace == "+":
        vysledek = cislo1 + cislo2
    elif operace == "-":
        vysledek = cislo1 - cislo2
    elif operace == "*":
        vysledek = cislo1 * cislo2
    elif operace == "/":
        if cislo2 == 0:
            print("Chyba: Dělení nulou není možné.")
            return
        vysledek = cislo1 / cislo2
    else:
        print("Chyba: Neplatná operace.")
        return

    # Zobrazení výsledku
    print(f"Výsledek: {cislo1} {operace} {cislo2} = {vysledek}")

    
# Spuštění kalkulačky
kalkulacka()