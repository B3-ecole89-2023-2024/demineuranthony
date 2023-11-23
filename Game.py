import random


def init_mine(w, h, b):
    tab = [0] * (w * h)

    for _ in range(b):
        while True:
            x, y = random.randrange(0, w), random.randrange(0, h)
            index = x + y * w

            if tab[index] == 0:
                tab[index] = -1
                break

    for x in range(h):
        for y in range(w):
            index = x * w + y

            if tab[index] == -1:
                continue

            distribute(tab, h, index, w, x, y)

    return [str(cell) if cell >= 0 else "X" for cell in tab]


def distribute(grid, height, index, width, x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < height and 0 <= y + j < width:
                if grid[(x + i) * width + (y + j)] == -1:
                    grid[index] += 1


def undercover(flag, x, y, width, height, displayed_map, mine_map):
    if x < 0 or x >= height or y < 0 or y >= width:
        return displayed_map
    index = x * width + y

    # Si le joueur veut poser un flag
    if flag == 2:
        displayed_map[index] = "⚑"
        return displayed_map

    # Si le joueur choisit une case flagué
    if displayed_map[index] == "⚑":
        return displayed_map

    if mine_map[index] == "X":
        lose = list('0')
        return lose
    elif int(mine_map[index]) > 0:
        displayed_map[index] = mine_map[index]
    elif displayed_map[index] != " ":
        displayed_map[index] = " "

        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < height and 0 <= y + j < width:
                    undercover(flag, x + i, y + j, width,
                               height, displayed_map, mine_map)
    return displayed_map


def selection(width, height, displayed_map, mine_map):
    x_selection = False
    print("\nVeuiller entrer la ligne (⮞) :")
    while not x_selection:
        try:
            x = int(input(">>> ")) - 1
            if -1 < x < width and x != '':
                x_selection = True
            else:
                print("Erreur, veuillez réessayer.")
        except:
            print("Erreur, veuillez réessayer.")

    y_selection = False
    print("\nVeuiller entrer la colonne (⮟) :")
    while not y_selection:
        try:
            y = int(input(">>> ")) - 1
            if -1 < y < height and y != '':
                y_selection = True
            else:
                print("Erreur, veuillez réessayer.")
        except:
            print("Erreur, veuillez réessayer.")

    flag_or_not = False
    print("""\nQuelle action souhaitez vous réaliser ?
    ---> Tape 1 pour déminer
    ---> Tape 2 pour poser un drapeau""")
    while not flag_or_not:
        flag = int(input(">>> "))
        if 0 < flag < 3:
            flag_or_not = True

    return undercover(flag, x, y, width, height, displayed_map, mine_map)
