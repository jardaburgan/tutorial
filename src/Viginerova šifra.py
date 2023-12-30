abeceda = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Zadejte text k zašifrování: ")
vstup = "moribundus"

print("Zadejte heslo: ")
heslo ="ab "

zasifrovana_zprava = ""

delka_hesla = len(heslo)
print(delka_hesla)

for znak in heslo:
    posun = abeceda.index(znak)
    print(posun)
    for znak in vstup:
        pozice_znaku = abeceda.index(znak)
        nova_pozice_znaku = pozice_znaku + posun
        novy_znak = abeceda[nova_pozice_znaku]
        zasifrovana_zprava += novy_znak



print(zasifrovana_zprava)