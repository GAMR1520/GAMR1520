number = input('Enter a number [1 - 12]: ')

# this will raise an error if a non-integer is entered
number = int(number)

if (number < 1):
    print("Invalid number (less than 1)")
elif(number > 12):
    print("Invalid number (greater than 12)")
else:
    print(tuple(range(number, number * 12 + 1, number)))
