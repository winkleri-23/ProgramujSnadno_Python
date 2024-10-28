# Jednoduchá Kalkulačka v Pythonu

Tento program představuje základní kalkulačku napsanou v jazyce Python, která umí provádět jednoduché aritmetické operace: sčítání, odčítání, násobení a dělení. Program běží v příkazové řádce a využívá vstupy od uživatele k provedení zvolené operace.

---

## Obsah

- [Začínáme](#začínáme)
- [Jak program funguje](#jak-program-funguje)
- [Průběh programu](#průběh-programu)
- [Ošetření chyb](#ošetření-chyb)
- [Příklad použití](#příklad-použití)
- [Požadavky](#požadavky)

---

## Začínáme

Aby bylo možné kalkulačku používat, je potřeba mít na svém systému nainstalovaný Python. Pokud Python ještě nemáte, můžete si ho stáhnout z [oficiální stránky Pythonu](https://www.python.org/downloads/).

---

## Jak program funguje

1. Program se spustí příkazem `kalkulacka()`, což zobrazí uvítací zprávu.
2. Uživateli se zobrazí výzva k zadání dvou čísel.
3. Po zadání čísel si uživatel vybere požadovanou operaci: `+` (sčítání), `-` (odčítání), `*` (násobení), nebo `/` (dělení).
4. Program provede výpočet podle zvolené operace a vypíše výsledek.

---

## Průběh programu

1. **Získání vstupů**: Program požádá uživatele o zadání dvou čísel a jedné operace.
2. **Výpočet**: Program provede operaci na zadaných číslech podle vstupu.
3. **Výstup výsledku**: Vypíše výsledek nebo chybovou zprávu (např. při dělení nulou).

---

## Ošetření chyb

- **Neplatná hodnota**: Pokud uživatel zadá nečíselnou hodnotu, program zobrazí chybovou zprávu.
- **Dělení nulou**: Pokud uživatel zvolí dělení a druhé číslo je 0, program zobrazí chybovou zprávu o nemožnosti dělení nulou.
- **Neplatná operace**: Pokud uživatel zadá jiný znak než `+`, `-`, `*` nebo `/`, program zobrazí chybovou zprávu o neplatné operaci.

---

## Příklad použití

```plaintext
Vítejte v kalkulačce!
Zadejte první číslo: 10
Zadejte druhé číslo: 5
Vyberte operaci (+, -, *, /): *
Výsledek: 10.0 * 5.0 = 50.0
