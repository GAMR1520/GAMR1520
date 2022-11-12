"""A program which tries to guess the number that you are thinking of"""

print("\n===================================")
print("Think of a number between 1 and 100")
print("Don't tell me".center(35))
print("===================================")
input("Press ENTER when you are ready.")

possible_range = (1, 100)
guesses = []
while True:
    guess = sum(possible_range) // 2
    guesses.append(guess)

    if input(f"\nIs it {guess}?\n [y/n] >> ").lower().startswith("y"):
        break

    if input(f"\nIs it greater than {guess}?\n [y/n] >> ").lower().startswith("y"):
        possible_range = (guess + 1, possible_range[1])
    else:
        possible_range = (possible_range[0], guess - 1)

print(f"\nI got it in {len(guesses)} guesses!\n")
print(guesses)