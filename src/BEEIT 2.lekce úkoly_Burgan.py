# # # Úkol 5.1 - Jednokolová hra Kámen, nůžky, papír
# #nahrání modulu pro práci s náhodou (počítač náhodně losuje symbol)
# import random
# #symboly, které bude počítač losovat a uživatel volit
# symboly = ["kámen", "nůžky", "papír"]
# #žádání uživatele o volbu symbolu
# symbol_hrac = input(f"Hrac1: zvol symbol {symboly}: ")
# #náhodné losování počítače z dodaného seznamu symbolů
# symbol_pocitac = random.choice(symboly)
# print(f"Počítač zvolil možnost {symbol_pocitac}.")
# #algoritmus hry kámen nůžky papír - DOPLŇTE
# if (symbol_hrac =="kámen" and symbol_pocitac == "kámen") or (symbol_hrac =="papír" and symbol_pocitac == "papír") or (symbol_hrac =="nůžky" and symbol_pocitac == "nůžky"):
#     print("Je to remíza.")
# elif (symbol_hrac =="kámen" and symbol_pocitac == "nůžky") or (symbol_hrac =="papír" and symbol_pocitac == "kámen") or (symbol_hrac =="nůžky" and symbol_pocitac == "papír"):
#     print("Vyhrál jsi!")
# elif (symbol_hrac =="kámen" and symbol_pocitac == "papír") or (symbol_hrac =="nůžky" and symbol_pocitac == "kámen") or (symbol_hrac =="papír" and symbol_pocitac == "nůžky"):
#     print("Prohrál jsi, vyhrál počítač!")


# # # Cvičení 5.2 - Registrace uživatele
# administratori = [("Admin", "Admin"), ("Reditel", "heslo")]
# uzivatele = [("Pepa", "123"), ("Jana", "t6Zyx3"), ("Richard", "risa55")]
# login_heslo = "Axdmin", "Admin"
#
# if administratori[0] == login_heslo or administratori[1] == login_heslo:
#     print("uděluji práva na úpravu ceny")
# elif uzivatele[0] == login_heslo or uzivatele[1] == login_heslo or uzivatele[2] == login_heslo:
#     print("uděluji práva na prohlížení produktů")
# else:
#     registrace = input("Chcete se registrovat (ano/ne)?")
#     if registrace == "ano":
#         uzivatele.append(login_heslo)
#         print("přidali jsme tě do seznamu uživatelů")
#     else:
#         print("Děkujeme za použití programu.")











