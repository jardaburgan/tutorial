alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# # BEZ FUNKCE
# if instruction == "encode":
#     for initial_letter_index in message:
#         new_letter_index = alphabet.index(initial_letter_index) + shift
#         if new_letter_index > 25:
#             # přetečení je možné vyřešit tím, že alphabet bude mít prvky 2x
#             new_letter_index = alphabet.index(initial_letter_index) + shift - 26
#         print(alphabet[new_letter_index], end="")
# elif instruction == "decode":
#     for initial_letter_index in message:
#         new_letter_index = alphabet.index(initial_letter_index) - shift
#         if new_letter_index < 0:
#             new_letter_index = alphabet.index(initial_letter_index) - shift + 26
#         print(alphabet[new_letter_index], end="")
# else:
#     print("Zadal si špatný příkaz, zkus znovu.")


def sifra (message, shift,instruction):
    new_text = ""
    for initial_letter in message:
        if initial_letter != " ":
            if instruction == "encode":
                new_letter_index = alphabet.index(initial_letter) + shift
                if new_letter_index > 25:
                    new_letter_index = alphabet.index(initial_letter) + shift - 26
                new_text += alphabet[new_letter_index]
            elif instruction == "decode":
                new_letter_index = alphabet.index(initial_letter) - shift
                if new_letter_index < 0:
                    new_letter_index = alphabet.index(initial_letter) - shift + 26
                new_text += alphabet[new_letter_index]
        else:
            new_text += initial_letter
    print(f"Nový text je {new_text}")

repeat = "yes"
while repeat == "yes":
    instruction = input("Zadej 'encode' abysi zašifroval text a nebo zadej 'decode', aby si dešifroval text\n")
    message = input ("Zadej zprávu\n").lower()
    shift = int(input ("Zadej posun\n"))
    sifra(message,shift,instruction)
    repeat = input("Napište yes pro pokračování a no pro konec programu.")