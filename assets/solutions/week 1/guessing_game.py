"""A programme which generates a random integer and asks the user to guess it"""

from random import randint

target = randint(1, 100)
msg = "Guess the number"

print()
print("=" * 20)
print("Guessing game")
print("=" * 20)
print()

while True:
    guess = int(input(f"{msg}:\n[1-100] >> "))        
    if guess == target:
        break
    if guess < target:
        msg = f"\nIt's higher than {guess}"
    else:
        msg = f"\nIt's lower than {guess}"

print("Well done!")
print(f"The number was {target}!")