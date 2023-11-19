import random

# Generování náhodného slova, které bychom měli uhádnout
resorts = ["amade", "kitzbuhel", "dachstein","hinterstoder", "pitztal"]
random_resort = resorts[random.randint(0,len(resorts)-1)]
# print(random_resort)

# Generování podtržítek místo písmenek a přehození listu do stringu
hidden_word = []
for one_letter in random_resort:
    hidden_word.append("_")
printedWord = ""
for one_letter in hidden_word:
    printedWord += one_letter
print(printedWord)

# Životy
lives = 6

# Hádání písmene a pokud jsem uhádl, tak dosadím místo podtržítka
while "_" in hidden_word:
    guess = input("Zadejte hádané písmeno\n").lower()
    for index in range(0,len(random_resort)):
        if guess == random_resort[index]:
            hidden_word[index] = guess

# Počítání a kontrola životů
    if guess not in random_resort:
        lives -= 1
    print(f"Počet Vašich životů je {lives}.")
    if lives == 0:
        print("Prohrál jsi!!!")
        break

# Vypsání zkrytého slova v normální podobě a ne jako list
    printedWord = ""
    for one_letter in hidden_word:
        printedWord +=one_letter
    print(printedWord)

    # Kontrola vítezství
    if "_" not in hidden_word:
        print("Vyhrál jsi!!!")