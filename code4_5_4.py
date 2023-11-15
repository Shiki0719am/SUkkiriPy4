for y in range(9):
    for x in range(9):
        anser = (y+1) * (x+1)
        print(f"{anser},",end=" ")
    print()

for y in range(9):
    for x in range(9):
        if (y + 1) % 2 == 0:
            continue
        anser = (y+1) * (x+1)
        print(f"{anser},",end="")
    print("\n")


for y in range(9):
    for x in range(9):
        if (y + 1) % 2 == 0:
            continue
        anser = (y+1) * (x+1)
        if anser > 50:
            break
        print(f"{anser},",end="")
    print("\n")
