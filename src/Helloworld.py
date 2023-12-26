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

