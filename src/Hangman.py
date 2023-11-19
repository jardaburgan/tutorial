import random

# Generování náhodného slova
resorts = ["amade", "kitzbuhel", "dachstein","hinterstoder", "pitztal"]
random_resort = resorts[random.randint(0,len(resorts)-1)]
print(random_resort)

# Generování podtržítek a přehození listu do stringu
hidden_word = []
for one_letter in random_resort:
    hidden_word.append("_")
printedWord = ""
for one_letter in hidden_word:
    printedWord += one_letter
print(printedWord)

# Hádání písmene a pokud jsem uhádl, tak dosadím místo podtržítka
while "_" in hidden_word:
    guess = input("Zadejte hádané písmeno\n").lower()
    for index in range(0,len(random_resort)):
        if guess == random_resort[index]:
            hidden_word[index] = guess
# Vypsání zkrytého slova v normální podobě a ne jako list
    printedWord = ""
    for one_letter in hidden_word:
        printedWord +=one_letter
    print(printedWord)
# Kontrola vítezství
if "_" not in hidden_word:
    print("Vyhrál jsi!!!")