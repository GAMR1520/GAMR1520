fname = "shopping.txt"

# read data from file
with open(fname, "r") as f:
    my_list = f.read().splitlines()

while True:
    print('=' * 20)
    print('shopping list'.center(20))
    print('-' * 20)
    for item in my_list or ("EMPTY LIST".center(20),):
        print(item)
    print('=' * 20)
    keep_going = input("add an item to the list? [y/n]")
    if not keep_going.lower().startswith('y'):
        break
    my_list += (input("New item: "),)

# write data back to file
with open(fname, "w") as f:
    for line in my_list:
        f.write(f"line\n")
