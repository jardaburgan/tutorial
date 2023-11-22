alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
instruction = input("Zadej 'encode' abysi zašifroval text a nebo zadej 'decode', aby si dešifroval text\n")
message = input ("Zadej zprávu\n")
shift = int(input ("Zadej posun\n"))


if instruction == "encode":
    for initial_letter_index in message:
        new_letter_index = alphabet.index(initial_letter_index) + shift
        if new_letter_index > 25:
            new_letter_index = alphabet.index(initial_letter_index) + shift - 26
        print(alphabet[new_letter_index], end="")
elif instruction == "decode":
    for initial_letter_index in message:
        new_letter_index = alphabet.index(initial_letter_index) - shift
        if new_letter_index < 0:
            new_letter_index = alphabet.index(initial_letter_index) - shift + 26
        print(alphabet[new_letter_index], end="")
else:
    print("Zadal si špatný příkaz, zkus znovu.")
