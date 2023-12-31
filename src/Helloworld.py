# # 1. SPOJOVÁNÍ ŘETEZCŮ
# vstup = input("Zadej něco, co chceš opakovat\n")
# vystup = vstup +" "+ vstup
# print(vystup)

# # 2. ZAOKROUHLOVÁNÍ
# cislo_a = float(input("Zadej číslo a"))
# cislo_b = float(input("Zadej číslo b"))
# result = cislo_a * cislo_b
# print(round(result,2))
# print(round(result,0))
# print(round(result,-1))

# # 3. MATEMATICKÉ OPERÁTORY
# x = 10
# y = 2
# # sčítání
# print(x + y)
# # odčítání
# print(x - y)
# # násobení
# print(x * y)
# # dělení
# print(x/y)
# # mocnění
# print(x**y)
# # modulo (zbytek při dělení)
# print(x%y)

# # 4. MODULY
# # decimal - datový typ desetiných čísel
# # fractions - modul na zlomky

# # 5. DATOVÉ TYPY
# # text: str
# # celé číslo: int
# # desetinné číslo: float, decimal z modulu decimal
# # pravda nebo nepravda: bool
# # zlomky: Fraction z modulu franctions
# from fractions import Fraction
# a = Fraction (3,4)
# b = Fraction (1,7)
# print(a+b)
# # funkce zobrazující datový typ: type

# # 6. TEXTOVÉ ŘETĚZCE
# prázdný_řetězec = " "
# prázdný_řetězec = ' '
# prázdný_řetězec = ''' '''
# #délka řetezce - len
# a = "jaroslav"
# print(len(a))
# # replikování (opakování) řetězců
# retezec = "Bum! "
# print(retezec * 7)
# # string.startswith(value, start, end): Vrátí TRUE, pokud string začíná definovaným textem
# vstup = "jaroslavek"
# print(vstup.startswith("jar"))
# print(vstup.startswith("ar",1,3))
# # string.endswith(value, start, end): Vrátí TRUE, pokud string končí definovaným textem
# # in: Ověření, zda se část textu nachází v řetezci
# vstup = "jaroslavek"
# print("osla" in vstup)
# # string.lower(): přehodí všechny znaky v řetězci na malá písmenka
# # string.upper(): přehodí všechny znaky v řetězci na velká písmenka
# name = "JARoslavek"
# print(name.upper())
# print(name.lower())
# # string.strip(): odstraní veškeré mezery v řetězci
# # string.replace(oldvalue, newvalue, count): nahradí část řetězce za jiný
# a = "Python je špatný"
# print(a.replace("špatný","dobrý"))
# # řezání řetězce seznam[m:n:i] - vybere m a každý i-tý znak do n-1, převrácení řetezce: [::-1]
# retezec = "honolulu"
# print(retezec[0])
# print(retezec[1:4])
# print(retezec[3:9:2])
# print(retezec[::-1])
# # find(): Metoda nám vrátí index první pozice podřetězce v jiném řetězci. Hledaný podřetězec předáváme jako parametr. Pokud není nalezen, vrátí -1.
# # index(): Metoda nám vrátí index první pozice podřetězce v jiném řetězci.Pokud nenalezne, vyvolá Valueerror
# # isalpha(): Metoda nám vrátí hodnotu True, pokud jsou všechny znaky v řetězci písmenné znaky
# # isdigit(): Metoda vrátí True, pokud jsou všechny znaky v řetězci číselné znaky (0 - 9)
# # islower(), isupper()

# # 7. PODMÍNKY A VĚTVENÍ
# a = 5
# b = 6
# if a > b:
#     print("Je to ok")
# elif a == b:
#     print ("OK")
# else: print("Dobrý")
# # match:
    # # case X:
# a = 5
# b = 4
# volba = "C"
# match volba:
#     case "A":
#         print(a+b)
#     case "B":
#         print(a-b)
#     case "C":
#         print(a*b)
# # match: propadávání - Case sjednotím pomocí znaku |
# mesic = 11
# match (mesic):
#     case 1 | 2 | 3:
#         print("Je první čtvrtletí.")
#     case 4 | 5 | 6:
#         print("Je druhé čtvrtletí.")
#     case 7 | 8 | 9:
#         print("Je třetí čtvrtletí.")
#     case 10 | 11 | 12:
#         print("Je čtvrté čtvrtletí.")
# # Ternární výraz: prvni_hodnota if (vyraz) else druha_hodnota
# muz = True
# nazev_pohlavi =  "muž" if (muz ) else "žena"
# print(nazev_pohlavi)

# # 8. CYKLY
# # for prvek in sekvence
# # range(začátek, konec, krok)
    # # range(n) - vrátí čísla od nuly do n-1 (do n,které už zahrnuto není)
    # # range(m, n) - vrátí čísla od m do n-1,
    # # range(m, n, i) - vrátí čísla od m a každé další i-té číslo do n-1
# # cyklus for
# for i in range(3):
#     print("Knock")
# for y in range(1,11,2):
#     print(y,end="")
# # cyklus for: násobilka
# for y in range(1,11):
#     for x in range(y,100,y):
#         print(y*x,end=" ")
#     print()
# # cyklus while
# # příkaz pass: cyklus se projede, ale nic se nevykoná
# for a in range(0,10):
#     pass
# print("Hotovo")
# # příkaz "break": ukončí aktuálně běžící cyklus
# # příkaz "continue": ukončí aktuální iteraci cyklu a ne celý cyklus jako "break"
# cisla_retezec = "10,50,abcd,30,9"
# cisla_seznam = cisla_retezec.split(',')
# soucet = 0
# for cislo in cisla_seznam:
#     if not cislo.isdigit():
#         continue
#     else:
#         cele_cislo = int(cislo)
#         soucet += cele_cislo
# print(f"Součet je: {soucet}")

# # 9. SEZNAM - list
# # deklarujeme pomocí []
# # převod sekvence do seznamu je pomocí funkce list()
# cisla = range(1,10)
# print(list(cisla[1:7:2]))
# # funkce len vrací počet prvků v seznamu
# # funkce enumerate vrací jak index prvku v seznamu, tak i samotný prvek
# cisla = [2,3,16,21]
# cisla.append(13)
# cisla.insert(1,10)
# cisla.extend([52,53,54])
# print(cisla)
# # list.remove: odstraní definovanou položku se seznamu
# cisla.remove(16)
# print(cisla)
# cisla.clear()
# print(cisla)
# # list.reverse(): otočí pořadí položek v seznamu tak, že první položka je nyní poslední
# # list.count(): vrátí počet výskytů definované položky
# cisla = [2,3,16,21,2,28,2]
# print(cisla.count(2))
# # list.sort(): seznam seřadí
# cisla = [2,3,16,21,2,28,2]
# cisla.sort()
# print(cisla)
# # list.index(): vrátí index prvního výskytu definované položky seznamu
# # funkce sorted(): vrátí setříděnou kopii původního seznamu
# cisla = [2,3,16,21,2,28,2]
# setridena_cisla = sorted(cisla)
# print(setridena_cisla)
# # převedení seznamu z formátu string na číselný formát
# seznam = ["2","3","16","21","2","28","2"]
# for i in range(0,len(seznam)):
#     seznam[i] = int(seznam[i])
# print(seznam)
# # split () - string.split(separator, maxsplit): rozdělí textový řetězec do seznamu (listu). Jako separátor je defaultně ",".
# # join () - string.join(iterable): vezme všechny podřetězce a spojí je do jednoho řetězce (stringu)

# # 10. FUNKCE
# # def "název funkce"("názvy argumentu(ů) funkce"):
# #    return
# # def mocnina(cislo):         # Cislo je název argumentu
# #    cislo = cislo ** 2
# #    return cislo
# # prvni_cislo = mocnina(2)    # Dvojka v závorce je námi dosazovaná hodnota argumentu
# # print(prvni_cislo)
# def soucin (x,y,z):
#     cislo = x * y * z
#     return cislo
# vypocet = soucin(2,5,8)
# print(vypocet)



















