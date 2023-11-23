import os


def displayMap(x, tab):
    cnt = 1
    output = """\n      """
    while cnt < x + 1:
        if cnt >= 10:
            output += f"""{cnt} """
        else:
            output += f""" {cnt} """
        cnt += 1

    output += "\n"
    cnt = 0
    char = 1

    while cnt < len(tab):
        if cnt % x == 0:
            if char > 9:
                output += f"""\n  {char}  """
            else:
                output += f"""\n  {char}   """
            char += 1
        output += f""" {tab[cnt]} """

        cnt += 1

    print(output)


def menu():
    print('\033c')
    print("""=== Menu Demineur === 
1. Nouvelle partie
2. Score
3. Règles du jeu
4. Quitter
""")
    choiceMenu()


def choiceMenu():
    choice = input("\nChoisissez une option : ")
    if choice == '1':
        print("Lancement d'une nouvelle partie")
    elif choice == '2':
        score()
    elif choice == '3':
        rule()
    elif choice == '4':
        byebye()


def score():
    scores = []
    if os.path.exists("score.txt"):
        with open("score.txt", 'r') as file:
            for line in file:
                print(line.strip())
    else:
        print('Aucun score encore enregistrer')

    return scores


def rule():
    print("""La règle du jeu est simple : le joueur sélectionne une case sur la grille, et cette case révèle un nombre qui indique le nombre de mines se trouvant dans les cases adjacentes. En utilisant ces informations, le joueur doit déduire l’emplacement des mines et les marquer avec des drapeaux pour les éviter.

La stratégie et la logique sont essentielles pour réussir au Démineur. Le joueur doit faire preuve de prudence et de réflexion pour éviter les cases piégées tout en découvrant les cases sûres. Chaque décision compte, car une erreur peut conduire à une explosion et à la fin de la partie.

En fonction de la taille de la grille et du nombre de mines, le niveaux de difficulté sera évolutif. Les joueurs peuvent également concourir pour obtenir le meilleur temps pour résoudre la grille ou le meilleur score en fonction de leur précision dans le marquage des mines.

Ce jeu captivant et stimulant met à l’épreuve les compétences analytiques et la prise de décision du joueur. Il offre une expérience de jeu addictive et satisfaisante pour les amateurs de puzzles et de défis intellectuels.""")


def byebye():
    print('Merci au revoir')


def selecteddifficulty():
    is_chosing = True
    difficulty()

    while is_chosing:
        scan = input(">>> ")
        if scan == "1":  # Facile
            is_chosing = False
            return 9, 9, 10
        elif scan == "2":  # Moyen
            is_chosing = False
            return 16, 16, 40
        elif scan == "3":  # Difficile
            is_chosing = False
            return 30, 16, 99
        else:
            print("Pas compris .  .  . \n")


def difficulty():
    print("""Choisissez une difficulté :
        ---> Tape 1 pour le mode facile
        ---> Tape 2 pour le mode moyen
        ---> Tape 3 pour le mode difficile
        """)
