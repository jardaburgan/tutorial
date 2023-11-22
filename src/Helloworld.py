number = int(input("Zadej celé kladné a číslo a já ti řeknu, zda je zadané číslo prvočíslo.\n"))

def prime_number_checker (number):
    result = "Je to provočíslo."
    for y in range(2,number):
        if number % y == 0:
            result = "Není to prvočíslo."
    print(result)

prime_number_checker(number)