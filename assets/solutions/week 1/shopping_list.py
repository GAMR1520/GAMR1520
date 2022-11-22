from pathlib import Path

path = Path("./shopping.txt")

# read data from file
with path.open("r") as f:
    shopping = f.read().splitlines()

width = 20
hline = '=' * width
while True:
    print(hline)
    print('shopping list'.center(width))
    print(hline)
    for item in shopping:
        print(item.center(width))
    print(hline)
    keep_going = input("add an item to the list? [y/n]")
    if not keep_going.lower().startswith('y'):
        break
    shopping += (input("New item: "),)

# write data back to file
with path.open("w") as f:
    for line in shopping:
        f.write(f"{line}\n")
