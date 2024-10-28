def kalkulacka():
    print("Vítejte v kalkulačce!")
    
    # Získání čísel od uživatele
    try:
        cislo1 = float(input("Zadejte první číslo: "))
        cislo2 = float(input("Zadejte druhé číslo: "))
    except ValueError:
        print("Chyba: Zadaná hodnota není číslo.")
        return

# Spuštění kalkulačky
kalkulacka()