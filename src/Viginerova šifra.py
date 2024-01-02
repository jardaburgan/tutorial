abeceda = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Zadejte text k zašifrování: ")
vstup = "moribundus"

print("Zadejte heslo: ")
heslo ="ahoj"

zasifrovana_zprava = ""
delka_hesla = len(heslo)
pozice_hesla = 0

for pismeno in vstup:
    # pokud je heslo kratší než šifrovaný text, jedu od začátku hesla
    if pozice_hesla == delka_hesla:
        pozice_hesla -= delka_hesla
    # naleznu index každého písmene ve vstupu
    stara_pozice = abeceda.index(pismeno)
    # definuji index šifrovaného znaku (písmene)
    nova_pozice = stara_pozice + (abeceda.index(heslo[pozice_hesla])) + 1
    # do zašifrované zprávy pošlu zašifrované písmeno
    zasifrovana_zprava += abeceda[nova_pozice]
    # posunu se v heslu o jeden znak dále a hledám následně index dalšího znaku v pořadí
    pozice_hesla +=1

print(zasifrovana_zprava)
