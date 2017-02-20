clothes = ["Jeans", "T-Shirt", "Skirt"]

for index in range(len(clothes)):
    print(clothes[index], end = "")
    if index != len(clothes) - 1:
        print(", ", end = "")
    else:
        print()

while True:
    choice = input("What do you want (CRUD)?")
    if choice.upper() == "D":
        position = int(input("Position?")) - 1
        print(position)
        del clothes[position]
        print(clothes)
    elif choice.upper() == "C":
        new_cloth = input("New item?")
        clothes.append(new_cloth)
        print(clothes)
