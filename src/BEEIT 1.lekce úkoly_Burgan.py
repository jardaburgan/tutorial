# # # Úkol 2 - Cena za salámy
# CENA_ZA_PALETU = 12  # Kc
# #získejte od uživatele počet palet salámu - DOPLŇTE
# pocet_palet_salamu = int(input("Kolik palet salámu si chceš koupit?\n"))
# #spočítejte celkovou cenu za počet požadovaný počet palet salámu - DOPLŇTE
# celkova_cena = int(CENA_ZA_PALETU) * pocet_palet_salamu
# #tisk ceny nákupu na obrazovku
# vypis = f"{pocet_palet_salamu} palet salámu ({CENA_ZA_PALETU} Kč za paletu) stojí {celkova_cena} Kč."
# print(vypis)


# # #Úkol 3 - Kalkulačka BMI
# #získání hmotnosti a výšky od uživatele - DOPLŇTE
# hmotnost = int(input("Zadej, kolik vážíš v kg: \n"))
# vyska = int(input("Zadej, kolik měříš v cm: \n"))
# #výpočet BMI - DOPLŇTE
# bmi = round(hmotnost / ((vyska/100)**2),2)
# print("Tvůj bmi index je: ")
# #tisk hodnoty BMI na obrazovku
# print(bmi)


# # #Úkol 4 - Spoření
# pocatecni_vklad = int(input("Zadej tvůj počáteční vklad v Kč: \n"))
# urok = float(input("zadej úrokovou sazbu v %: \n"))
# obdobi = int(input("Zadej počet let, na které vklad uložíš: \n"))
# vklad = round(pocatecni_vklad * (1 + (obdobi * urok/100)),2)
# print(f"Naspoříš si celkově {vklad} Kč.")