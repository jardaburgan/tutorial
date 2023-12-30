# řetězec, který chceme dekódovat
sifrovana_zprava = ".-.. . --- -. .- .-. -.. ---"
print(f"Původní zpráva: {sifrovana_zprava}")
# řetězec s dekódovanou zprávou
zprava = ""

# vzorová sekvence
abecedni_znaky = "abcdefghijklmnopqrstuvwxyz"
morseovy_znaky = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
"..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-",
"...-", ".--", "-..-", "-.--", "--.."]

# přehození šifrované zprávy do seznamu (listu znaků)
znaky = sifrovana_zprava.split(" ")

for znak in znaky:
    # nalezení indexu znaku v šifrované zprávě
    index_znaku = morseovy_znaky.index(znak)
    # nalezení písmena z abecedy dle indexu
    pismeno = abecedni_znaky[index_znaku]
    # přidání nalezeného písmene do výsledku
    zprava += pismeno

print(zprava)