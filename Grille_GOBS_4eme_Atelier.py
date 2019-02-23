# ======================================================================================================================
#             _____  ____  ____   _____    _______     _________ _    _  ____  _   _
#            / ____|/ __ \|  _ \ / ____|  |  __ \ \   / /__   __| |  | |/ __ \| \ | |
#           | |  __| |  | | |_) | (___    | |__) \ \_/ /   | |  | |__| | |  | |  \| |
#           | | |_ | |  | |  _ < \___ \   |  ___/ \   /    | |  |  __  | |  | | . ` |
#           | |__| | |__| | |_) |____) |  | |      | |     | |  | |  | | |__| | |\  |
#            \_____|\____/|____/|_____/   |_|      |_|     |_|  |_|  |_|\____/|_| \_|
#
# ======================================================================================================================
#
#       Plan du code :
#
#       - FONCTIONS INTERFACES
#       - JEUX DE TESTS
#       - FONCTIONS DEPLACEMENTS DROITES
#       - FONCTIONS DEPLACEMENTS DIAGONALES
#       - FONCTIONS DEPLACEMENTS ET DESTINATIONS
#       - FONCTIONS TOUR DE JEU ET FIN DE JEU
#       - MAIN
#
# =======================================================================================================================
#                 ___       _             __
#                |_ _|_ __ | |_ ___ _ __ / _| __ _  ___ ___
#                 | || '_ \| __/ _ \ '__| |_ / _` |/ __/ _ \
#                 | || | | | ||  __/ |  |  _| (_| | (_|  __/
#                |___|_| |_|\__\___|_|  |_|  \__,_|\___\___|
#
# =======================================================================================================================

import random
random.seed()

"""  FONCTIONS INTERFACES  """

#affichage de "joueur 1 : O" et "joueur 2 : X"
def joueur(grille):
    n = 0
    pions_o = 0
    pions_x = 0

    #on parcours la liste grille sur les 9 colonnes
    while n <= 8:
        for element in grille[0 + n]:
            #si l'element dans la liste grille est un 1, on incrémente de 1 le pion_o
            if element == 1:
                pions_o = pions_o + 1

            #si l'element dans la liste grille est un 2, on incrémente de 1 le pion_x
            if element == 2:
                pions_x = pions_x + 1
        n = n + 1

    print('    Joueur O :', pions_o, '      Joueur X : ', pions_x)
    print('')

    return pions_o, pions_x


#on définie la fonction qui va créer la grille
def creation_grille(grille):

    numero_ligne = 0
    print('\ y  0   1   2   3   4   5   6   7   8\nx')
    print('   +---+---+---+---+---+---+---+---+---+')

    #en fonction de la liste de la grille, on va créer l'interface de la grille
    for ligne in grille:
        print(numero_ligne, ' |', end='')
        numero_colonne = 0

        for colonne in ligne:
            if numero_colonne < 8:
                if grille[numero_ligne][numero_colonne] == 0:
                    print('   |', end='')
                elif grille[numero_ligne][numero_colonne] == 1:
                    print(' O |', end='')
                elif grille[numero_ligne][numero_colonne] == 2:
                    print(' X |', end='')

            else:
                if grille[numero_ligne][numero_colonne] == 0:
                    print('   |')
                elif grille[numero_ligne][numero_colonne] == 1:
                    print(' O |')
                elif grille[numero_ligne][numero_colonne] == 2:
                    print(' X |')

                print('   +---+---+---+---+---+---+---+---+---+')
            numero_colonne += 1
        numero_ligne += 1


#fonction qui demande au joueur la configuration voulue
def type_partie(creation_grille):

    print('Debut, Milieu ou Fin de partie ? D / M / F')
    type = str(input())

    #le programme boucle tant que les lettres entrées sont incorrectes
    while type != 'd' and type != 'D' and type != 'm' and type != 'M' and type != 'f' and type != 'F':

        print('Debut, Milieu ou Fin de partie ? D / M / F')
        type = str(input())

    if type == 'd' or type == 'D':
        #affichage début de partie
        grille = [[1, 1, 1, 1, 1, 1, 1, 1, 1], 
                  [1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                  [2, 2, 2, 2, 2, 2, 2, 2, 2],
                  [2, 2, 2, 2, 2, 2, 2, 2, 2], 
                  [2, 2, 2, 2, 2, 2, 2, 2, 2]]

        creation_grille(grille)
        return grille

    elif type == 'm' or type == 'M':
        #affichage milieu de partie
        grille = [[0, 0, 0, 1, 0, 0, 0, 1, 2], 
                  [1, 0, 2, 2, 1, 0, 0, 0, 0],
                  [2, 1, 1, 0, 0, 0, 0, 0, 1], 
                  [0, 0, 0, 0, 0, 1, 1, 1, 2], 
                  [0, 1, 2, 1, 2, 2, 2, 0, 0], 
                  [0, 2, 1, 0, 1, 2, 1, 0, 0], 
                  [2, 1, 2, 0, 0, 0, 1, 0, 2],
                  [2, 1, 0, 1, 0, 1, 0, 2, 0], 
                  [0, 0, 1, 0, 2, 0, 1, 0, 1]]

        creation_grille(grille)
        return grille

    elif type == 'f' or type == 'F':
        #affichage fin de partie
        grille = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 2, 0, 1, 0, 1, 2, 0],
                  [0, 0, 1, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 2, 0, 2, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 1, 0], 
                  [0, 0, 2, 0, 1, 0, 0, 0, 0], 
                  [0, 0, 0, 2, 0, 0, 0, 2, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 1, 0, 0, 0, 0, 1, 0]]

        creation_grille(grille)
        return grille


"""  JEUX DE TESTS  """

#saisie de coordonnées pour tester si la case saisie est dans la grille
def est_dans_grille():

    print('"""  TEST DE COORDONNEES DANS LA GRILLE  ""')
    print('\nVeuillez saisir le numéro de ligne (x)')
    ligne = int(input())

    print('Veuillez saisir le numéro de colonne (y)')
    colonne = int(input())

    if ligne < 0 or ligne > 8 or colonne < 0 or colonne > 8:
        print("\nla case saisie n'est pas dans la grille\n")
        return True

    else:
        print("\nla case saisie est bien dans la grille\n")
        return False


# =======================================================================================================================
#                 ____             _                                     _
#                |  _ \  ___ _ __ | | __ _  ___ ___ _ __ ___   ___ _ __ | |_ ___
#                | | | |/ _ \ '_ \| |/ _` |/ __/ _ \ '_ ` _ \ / _ \ '_ \| __/ __|
#                | |_| |  __/ |_) | | (_| | (_|  __/ | | | | |  __/ | | | |_\__ \
#                |____/ \___| .__/|_|\__,_|\___\___|_| |_| |_|\___|_| |_|\__|___/
#                           |_|
# =======================================================================================================================

"""  FONCTIONS DEPLACEMENTS DROITES  """


def choix_pion_deplacement(grille, tour_o, tour_x):
    
    destination_totaux_possibles = []

    print('Veuillez saisir la ligne du pion à déplacer (x)')
    x1 = int(input())
    print('Veuillez saisir la colonne du pion à déplacer (y)')
    y1 = int(input())
    #on indique les coordonnées saisies par le joueur
    print('Vous avez choisi le pion en : [', x1, ',', y1, ']')
    
    if tour_x:
        #on s'assure que si la case choisie contient le pion x au tour x
        while x1 < 0 or x1 > 8 or y1 < 0 or y1 > 8 or grille[x1][y1] != 2:
            print("!! Choix du pion invalide !!")
            print('Veuillez saisir la ligne du pion à déplacer (x)')
            x1 = int(input())
            print('Veuillez saisir la colonne du pion à déplacer (y)')
            y1 = int(input())
            print('Vous avez choisi le pion en : [', x1, ',', y1, ']')

    elif tour_o:
        #on s'assure que si la case choisie contient le pion o au tour o
        while x1 < 0 or x1 > 8 or y1 < 0 or y1 > 8 or grille[x1][y1] != 1:
            print("!! Choix du pion invalide !!")
            print('Veuillez saisir la ligne du pion à déplacer (x)')
            x1 = int(input())
            print('Veuillez saisir la colonne du pion à déplacer (y)')
            y1 = int(input())
            print('Vous avez choisi le pion en : [', x1, ',', y1, ']')

    return x1, y1, destination_totaux_possibles


#fonction déplacement vers le haut
def deplacement_haut(x1, y1, grille, destination_totaux_possibles, tour_x, tour_o):

    destination_haut_possible = []
    case_suivante = 1
    
    #si c'est au tour x, les allies sont 2 et ennemi sont 1 (dans la grille)
    if tour_x:
        allie, ennemi = 2, 1
    
    elif tour_o:
        allie, ennemi = 1, 2

    #tant que le deplacement vers le haut n'est pas gêné par un obstacle
    while x1 - case_suivante > 0 and grille[x1 - case_suivante][y1] != allie:
        #si la case possible est 0, on peut se déplacer
        if grille[x1 - case_suivante][y1] == 0:
            destination_haut_possible.append([x1 - case_suivante, y1])
            destination_totaux_possibles.append([x1 - case_suivante, y1])

        #sinon si on rencontre un ennemi et que la case d'apres est libre, on peut effectuer un "saut"
        elif grille[x1 - case_suivante][y1] == ennemi and grille[(x1 - 1) - case_suivante][y1] == 0:
            #on ajoute la case d'apres dans les possibilités et on arrete de parcourir la grille
            destination_haut_possible.append([(x1 - 1) - case_suivante, y1])
            destination_totaux_possibles.append([(x1 - 1) - case_suivante, y1])
            break

        #sinon, si on rencontre un ennemi sans case libre derriere, on peut faire une "élimination"
        elif grille[x1 - case_suivante][y1] == ennemi and grille[(x1 - 1) - case_suivante][y1] != 0:
            destination_haut_possible.append([x1 - case_suivante, y1])
            destination_totaux_possibles.append([x1 - case_suivante, y1])
            break
        
        #on actualise la case à traiter
        case_suivante += 1
    
    #on traite le cas des cases au bord de la grille
    if grille[x1 - case_suivante][y1] != allie and x1 - case_suivante >= 0:
        #on ajoute la case du bord si il n'y a pas d'ennemis sur celle-ci
        destination_haut_possible.append([x1 - case_suivante, y1])
        destination_totaux_possibles.append([x1 - case_suivante, y1])
    
    #dans certaines conditions, notre programme affiche 2 fois les mêmes cases, on supprime donc une des cases identiques
    if len(destination_haut_possible) >= 2 and destination_haut_possible[-1] == destination_haut_possible[-2]:
        destination_haut_possible.remove(destination_haut_possible[-1])
        destination_totaux_possibles.remove(destination_totaux_possibles[-1])

    print('\nDeplacement haut   :', destination_haut_possible)


#fonction déplacement vers le bas
def deplacement_bas(x1, y1, grille, destination_totaux_possibles, tour_x, tour_o):

    destination_bas_possible = []
    case_suivante = 1

    #si c'est au tour x, les allies sont 2 et ennemi sont 1 (dans la grille)
    if tour_x:
        allie, ennemi = 2, 1
    
    elif tour_o:
        allie, ennemi = 1, 2

    #tant que le deplacement vers le bas n'est pas gêné par un obstacle
    while x1 + case_suivante < 8 and grille[x1 + case_suivante][y1] != allie:
        #si la case possible est 0, on peut se déplacer
        if grille[x1 + case_suivante][y1] == 0:
            destination_bas_possible.append([x1 + case_suivante, y1])
            destination_totaux_possibles.append([x1 + case_suivante, y1])

        #sinon si on rencontre un ennemi et que la case d'apres est libre, on peut effectuer un "saut"
        elif grille[x1 + case_suivante][y1] == ennemi and grille[(x1 + 1) + case_suivante][y1] == 0:
            #on ajoute la case d'apres dans les possibilités et on arrete de parcourir la grille
            destination_bas_possible.append([(x1 + 1) + case_suivante, y1])
            destination_totaux_possibles.append([(x1 + 1) + case_suivante, y1])
            break

        #sinon, si on rencontre un ennemi sans case libre derriere, on peut faire une "élimination"
        elif grille[x1 + case_suivante][y1] == ennemi and grille[(x1 + 1) + case_suivante][y1] != 0:
            destination_bas_possible.append([x1 + case_suivante, y1])
            destination_totaux_possibles.append([x1 + case_suivante, y1])
            break
        
        #on actualise la case à traiter
        case_suivante += 1
    
    #on traite le cas des cases au bord de la grille
    if x1 + case_suivante <= 8 and grille[x1 + case_suivante][y1] != allie:
        #on ajoute la case du bord si il n'y a pas d'ennemis sur celle-ci
        destination_bas_possible.append([x1 + case_suivante, y1])
        destination_totaux_possibles.append([x1 + case_suivante, y1])
    
    #dans certaines conditions, notre programme affiche 2 fois les mêmes cases, on supprime donc une des cases identiques
    if len(destination_bas_possible) >= 2 and destination_bas_possible[-1] == destination_bas_possible[-2]:
        destination_bas_possible.remove(destination_bas_possible[-1])
        destination_totaux_possibles.remove(destination_totaux_possibles[-1])

    print('Deplacement bas    :', destination_bas_possible)


#fonction déplacement vers la gauche
def deplacement_gauche(x1, y1, grille, destination_totaux_possibles, tour_x, tour_o):

    destination_gauche_possible = []
    case_suivante = 1

    #si c'est au tour x, les allies sont 2 et ennemi sont 1 (dans la grille)
    if tour_x:
        allie, ennemi = 2, 1
    
    elif tour_o:
        allie, ennemi = 1, 2

    #tant que le deplacement vers la gauche n'est pas gêné par un obstacle
    while y1 - case_suivante > 0 and grille[x1][y1 - case_suivante] != allie:
        #si la case possible est 0, on peut se déplacer
        if grille[x1][y1 - case_suivante] == 0:
            destination_gauche_possible.append([x1, y1 - case_suivante])
            destination_totaux_possibles.append([x1, y1 - case_suivante])

        #sinon si on rencontre un ennemi et que la case d'apres est libre, on peut effectuer un "saut"
        elif grille[x1][y1 - case_suivante] == ennemi and grille[x1][(y1 - 1) - case_suivante] == 0:
            #on ajoute la case d'apres dans les possibilités et on arrete de parcourir la grille
            destination_gauche_possible.append([x1, (y1 - 1) - case_suivante])
            destination_totaux_possibles.append([x1, (y1 - 1) - case_suivante])
            break

        #sinon, si on rencontre un ennemi sans case libre derriere, on peut faire une "élimination"
        elif grille[x1][y1 - case_suivante] == ennemi and grille[x1][(y1 - 1) - case_suivante] != 0:
            destination_gauche_possible.append([x1, y1 - case_suivante])
            destination_totaux_possibles.append([x1, y1 - case_suivante])
            break
        
        #on actualise la case à traiter
        case_suivante += 1
    
    #on traite le cas des cases au bord de la grille
    if y1 - case_suivante >= 0 and grille[x1][y1 - case_suivante] != allie:
        #on ajoute la case du bord si il n'y a pas d'ennemis sur celle-ci
        destination_gauche_possible.append([x1, y1 - case_suivante])
        destination_totaux_possibles.append([x1, y1 - case_suivante])
    
    #dans certaines conditions, notre programme affiche 2 fois les mêmes cases, on supprime donc une des cases identiques
    if len(destination_gauche_possible) >= 2 and destination_gauche_possible[-1] == destination_gauche_possible[-2]:
        destination_gauche_possible.remove(destination_gauche_possible[-1])
        destination_totaux_possibles.remove(destination_totaux_possibles[-1])

    print('Deplacement gauche :', destination_gauche_possible)


#fonction déplacement vers la droite
def deplacement_droite(x1, y1, grille, destination_totaux_possibles, tour_x, tour_o):

    destination_droite_possible = []
    case_suivante = 1

    #si c'est au tour x, les allies sont 2 et ennemi sont 1 (dans la grille)
    if tour_x:
        allie, ennemi = 2, 1
    
    elif tour_o:
        allie, ennemi = 1, 2

    #tant que le deplacement vers la droite n'est pas gêné par un obstacle
    while y1 + case_suivante < 8 and grille[x1][y1 + case_suivante] != allie:
        #si la case possible est 0, on peut se déplacer
        if grille[x1][y1 + case_suivante] == 0:
            destination_droite_possible.append([x1, y1 + case_suivante])
            destination_totaux_possibles.append([x1, y1 + case_suivante])

        #sinon si on rencontre un ennemi et que la case d'apres est libre, on peut effectuer un "saut"
        elif grille[x1][y1 + case_suivante] == ennemi and grille[x1][(y1 + 1) + case_suivante] == 0:
            #on ajoute la case d'apres dans les possibilités et on arrete de parcourir la grille
            destination_droite_possible.append([x1, (y1 + 1) + case_suivante])
            destination_totaux_possibles.append([x1, (y1 + 1) + case_suivante])
            break

        #sinon, si on rencontre un ennemi sans case libre derriere, on peut faire une "élimination"
        elif grille[x1][y1 + case_suivante] == ennemi and grille[x1][(y1 + 1) + case_suivante] != 0:
            destination_droite_possible.append([x1, y1 + case_suivante])
            destination_totaux_possibles.append([x1, y1 + case_suivante])
            break
        
        #on actualise la case à traiter
        case_suivante += 1
    
    #on traite le cas des cases au bord de la grille
    if y1 + case_suivante <= 8 and grille[x1][y1 + case_suivante] != allie:
        #on ajoute la case du bord si il n'y a pas d'ennemis sur celle-ci
        destination_droite_possible.append([x1, y1 + case_suivante])
        destination_totaux_possibles.append([x1,y1 + case_suivante])
    
    #dans certaines conditions, notre programme affiche 2 fois les mêmes cases, on supprime donc une des cases identiques
    if len(destination_droite_possible) >= 2 and destination_droite_possible[-1] == destination_droite_possible[-2]:
        destination_droite_possible.remove(destination_droite_possible[-1])
        destination_totaux_possibles.remove(destination_totaux_possibles[-1])

    print('Deplacement droite :', destination_droite_possible, '\n')


"""  FONCTIONS DEPLACEMENTS DIAGONALES  """


#création de la fonction case déplacement diagonale haut gauche possible
def diago_haut_gauche(x1, y1, grille, destination_totaux_possibles, tour_x, tour_o):

    destination_haut_gauche_possible = []
    case_suivante = 1

    #si c'est au tour x, les allies sont 2 et ennemi sont 1 (dans la grille)
    if tour_x:
        allie, ennemi = 2, 1
    
    elif tour_o:
        allie, ennemi = 1, 2

    #tant que le deplacement vers le haut gauche n'est pas gêné par un obstacle
    while x1 - case_suivante > 0 and y1 - case_suivante > 0 and grille[x1 - case_suivante][y1 - case_suivante] != allie:
        #si la case possible est 0, on peut se déplacer
        if grille[x1 - case_suivante][y1 - case_suivante] == 0:
            destination_haut_gauche_possible.append([x1 - case_suivante, y1 - case_suivante])
            destination_totaux_possibles.append([x1 - case_suivante, y1 - case_suivante])

        #sinon si on rencontre un ennemi et que la case d'apres est libre, on peut effectuer un "saut"
        elif grille[x1 - case_suivante][y1 - case_suivante] == ennemi and grille[(x1 - 1) - case_suivante][(y1 - 1) - case_suivante] == 0:
            #on ajoute la case d'apres dans les possibilités et on arrete de parcourir la grille
            destination_haut_gauche_possible.append([(x1 - 1) - case_suivante, (y1 - 1) - case_suivante])
            destination_totaux_possibles.append([(x1 - 1) - case_suivante, (y1 - 1) - case_suivante])
            break

        #sinon, si on rencontre un ennemi sans case libre derriere, on peut faire une "élimination"
        elif grille[x1 - case_suivante][y1 - case_suivante] == ennemi and grille[(x1 - 1) - case_suivante][(y1 - 1) - case_suivante] != 0:
            destination_haut_gauche_possible.append([x1 - case_suivante, y1  - case_suivante])
            destination_totaux_possibles.append([x1 - case_suivante, y1 - case_suivante])
            break
        
        #on actualise la case à traiter
        case_suivante += 1
    
    #on traite le cas des cases au bord de la grille
    if grille[x1 - case_suivante][y1 - case_suivante] != allie and x1 - case_suivante >= 0 and y1 - case_suivante >= 0:
        #on ajoute la case du bord si il n'y a pas d'ennemis sur celle-ci
        destination_haut_gauche_possible.append([x1 - case_suivante, y1 - case_suivante])
        destination_totaux_possibles.append([x1 - case_suivante, y1 - case_suivante])
    
    #dans certaines conditions, notre programme affiche 2 fois les mêmes cases, on supprime donc une des cases identiques
    if len(destination_haut_gauche_possible) >= 2 and destination_haut_gauche_possible[-1] == destination_haut_gauche_possible[-2]:
        destination_haut_gauche_possible.remove(destination_haut_gauche_possible[-1])
        destination_totaux_possibles.remove(destination_totaux_possibles[-1])

    print('Deplacement diagonal haut gauche :', destination_haut_gauche_possible)


#création de la fonction case déplacement diagonale haut droite possible
def diago_haut_droite(x1, y1, grille, destination_totaux_possibles, tour_x, tour_o):

    destination_haut_droite_possible = []
    case_suivante = 1

    #si c'est au tour x, les allies sont 2 et ennemi sont 1 (dans la grille)
    if tour_x:
        allie, ennemi = 2, 1
    
    elif tour_o:
        allie, ennemi = 1, 2
    
    #tant que le deplacement vers le haut droite n'est pas gêné par un obstacle
    while x1 - case_suivante > 0 and y1 + case_suivante < 8 and grille[x1 - case_suivante][y1 + case_suivante] != allie:
        #si la case possible est 0, on peut se déplacer
        if grille[x1 - case_suivante][y1 + case_suivante] == 0:
            destination_haut_droite_possible.append([x1 - case_suivante, y1 + case_suivante])
            destination_totaux_possibles.append([x1 - case_suivante, y1 + case_suivante])

        #sinon si on rencontre un ennemi et que la case d'apres est libre, on peut effectuer un "saut"
        elif grille[x1 - case_suivante][y1 + case_suivante] == ennemi and grille[(x1 - 1) - case_suivante][(y1 + 1) + case_suivante] == 0:
            #on ajoute la case d'apres dans les possibilités et on arrete de parcourir la grille
            destination_haut_droite_possible.append([(x1 - 1) - case_suivante, (y1 + 1) + case_suivante])
            destination_totaux_possibles.append([(x1 - 1) - case_suivante, (y1 + 1) + case_suivante])
            break

        #sinon, si on rencontre un ennemi sans case libre derriere, on peut faire une "élimination"
        elif grille[x1 - case_suivante][y1 + case_suivante] == ennemi and grille[(x1 - 1) - case_suivante][(y1 + 1) + case_suivante] != 0:
            destination_haut_droite_possible.append([x1 - case_suivante, y1  + case_suivante])
            destination_totaux_possibles.append([x1 - case_suivante, y1 + case_suivante])
            break
        
        #on actualise la case à traiter
        case_suivante += 1
    
    #on traite le cas des cases au bord de la grille
    if x1 - case_suivante >= 0 and y1 + case_suivante <= 8 and grille[x1 - case_suivante][y1 + case_suivante] != allie:
        #on ajoute la case du bord si il n'y a pas d'ennemis sur celle-ci
        destination_haut_droite_possible.append([x1 - case_suivante, y1 + case_suivante])
        destination_totaux_possibles.append([x1 - case_suivante, y1 + case_suivante])
    
    #dans certaines conditions, notre programme affiche 2 fois les mêmes cases, on supprime donc une des cases identiques
    if len(destination_haut_droite_possible) >= 2 and destination_haut_droite_possible[-1] == destination_haut_droite_possible[-2]:
        destination_haut_droite_possible.remove(destination_haut_droite_possible[-1])
        destination_totaux_possibles.remove(destination_totaux_possibles[-1])
    
    print('Deplacement diagonal haut droite :', destination_haut_droite_possible)


#création de la fonction case déplacement diagonale bas gauche possible
def diago_bas_gauche(x1, y1, grille, destination_totaux_possibles, tour_x, tour_o):

    destination_bas_gauche_possible = []
    case_suivante = 1

    #si c'est au tour x, les allies sont 2 et ennemi sont 1 (dans la grille)
    if tour_x:
        allie, ennemi = 2, 1
    
    elif tour_o:
        allie, ennemi = 1, 2

    #tant que le deplacement vers le bas gauche n'est pas gêné par un obstacle
    while x1 + case_suivante < 8 and y1 - case_suivante > 0 and grille[x1 + case_suivante][y1 - case_suivante] != allie:
        #si la case possible est 0, on peut se déplacer
        if grille[x1 + case_suivante][y1 - case_suivante] == 0:
            destination_bas_gauche_possible.append([x1 + case_suivante, y1 - case_suivante])
            destination_totaux_possibles.append([x1 + case_suivante, y1 - case_suivante])

        #sinon si on rencontre un ennemi et que la case d'apres est libre, on peut effectuer un "saut"
        elif grille[x1 + case_suivante][y1 - case_suivante] == ennemi and grille[(x1 + 1) + case_suivante][(y1 - 1) - case_suivante] == 0:
            #on ajoute la case d'apres dans les possibilités et on arrete de parcourir la grille
            destination_bas_gauche_possible.append([(x1 + 1) + case_suivante, (y1 - 1) - case_suivante])
            destination_totaux_possibles.append([(x1 + 1) + case_suivante, (y1 - 1) - case_suivante])
            break

        #sinon, si on rencontre un ennemi sans case libre derriere, on peut faire une "élimination"
        elif grille[x1 + case_suivante][y1 - case_suivante] == ennemi and grille[(x1 + 1) + case_suivante][(y1 - 1) - case_suivante] != 0:
            destination_bas_gauche_possible.append([x1 + case_suivante, y1  - case_suivante])
            destination_totaux_possibles.append([x1 + case_suivante, y1 - case_suivante])
            break
        
        #on actualise la case à traiter
        case_suivante += 1
    
    #on traite le cas des cases au bord de la grille
    if x1 + case_suivante <= 8 and y1 - case_suivante >= 0 and grille[x1 + case_suivante][y1 - case_suivante] != allie:
        #on ajoute la case du bord si il n'y a pas d'ennemis sur celle-ci
        destination_bas_gauche_possible.append([x1 + case_suivante, y1 - case_suivante])
        destination_totaux_possibles.append([x1 + case_suivante, y1 - case_suivante])
    
    #dans certaines conditions, notre programme affiche 2 fois les mêmes cases, on supprime donc une des cases identiques
    if len(destination_bas_gauche_possible) >= 2 and destination_bas_gauche_possible[-1] == destination_bas_gauche_possible[-2]:
        destination_bas_gauche_possible.remove(destination_bas_gauche_possible[-1])
        destination_totaux_possibles.remove(destination_totaux_possibles[-1])

    print('Deplacement diagonal bas gauche  :', destination_bas_gauche_possible)


#création de la fonction case déplacement diagonale bas droite possible
def diago_bas_droite(x1, y1, grille, destination_totaux_possibles, tour_x, tour_o):

    destination_bas_droite_possible = []
    case_suivante = 1

    #si c'est au tour x, les allies sont 2 et ennemi sont 1 (dans la grille)
    if tour_x:
        allie, ennemi = 2, 1
    
    elif tour_o:
        allie, ennemi = 1, 2

    #tant que le deplacement vers le bas droite n'est pas gêné par un obstacle
    while x1 + case_suivante < 8 and y1 + case_suivante < 8 and grille[x1 + case_suivante][y1 + case_suivante] != allie:
        #si la case possible est 0, on peut se déplacer
        if grille[x1 + case_suivante][y1 + case_suivante] == 0:
            destination_bas_droite_possible.append([x1 + case_suivante, y1 + case_suivante])
            destination_totaux_possibles.append([x1 + case_suivante, y1 + case_suivante])

        #sinon si on rencontre un ennemi et que la case d'apres est libre, on peut effectuer un "saut"
        elif grille[x1 + case_suivante][y1 + case_suivante] == ennemi and grille[(x1 + 1) + case_suivante][(y1 + 1) + case_suivante] == 0:
            #on ajoute la case d'apres dans les possibilités et on arrete de parcourir la grille
            destination_bas_droite_possible.append([(x1 + 1) + case_suivante, (y1 + 1) + case_suivante])
            destination_totaux_possibles.append([(x1 + 1) + case_suivante, (y1 + 1) + case_suivante])
            break

        #sinon, si on rencontre un ennemi sans case libre derriere, on peut faire une "élimination"
        elif grille[x1 + case_suivante][y1 + case_suivante] == ennemi and grille[(x1 + 1) + case_suivante][(y1 + 1) + case_suivante] != 0:
            destination_bas_droite_possible.append([x1 + case_suivante, y1  + case_suivante])
            destination_totaux_possibles.append([x1 + case_suivante, y1 + case_suivante])
            break
        
        #on actualise la case à traiter
        case_suivante += 1
    
    #on traite le cas des cases au bord de la grille
    if x1 + case_suivante <= 8 and y1 + case_suivante <= 8 and grille[x1 + case_suivante][y1 + case_suivante] != allie:
        destination_bas_droite_possible.append([x1 + case_suivante, y1 + case_suivante])
        destination_totaux_possibles.append([x1 + case_suivante, y1 + case_suivante])

    
    #dans certaines conditions, notre programme affiche 2 fois les mêmes cases, on supprime donc une des cases identiques
    if len(destination_bas_droite_possible) >= 2 and destination_bas_droite_possible[-1] == destination_bas_droite_possible[-2]:
        destination_bas_droite_possible.remove(destination_bas_droite_possible[-1])
        destination_totaux_possibles.remove(destination_totaux_possibles[-1])

    print('Deplacement diagonal bas droite  :', destination_bas_droite_possible)


"""   FONCTIONS DEPLACEMENTS ET DESTINATIONS   """


#appel des fonctions déplacements possibles
def deplacement(grille, x1, y1, x2, y2, destination_totaux_possibles, tour_x, tour_o, pions_o, pions_x):

    destination_totaux_possibles = []
    destination_totaux_possibles = execution_deplacement(
        grille, x1, y1, destination_totaux_possibles, tour_x, tour_o)
    #appel de la fonction destination voulue

    while destination_totaux_possibles != [] or grille[x1][y1] == 0:

        #apres avoir changé de place, on actualise la grille
        grille, x2, y2 = fonction_destination(destination_totaux_possibles, x1, y1, grille)
        x1, y1, x2, y2 = x2, y2, x1, y1

        #on enleve l'ennemi si on a effectué une elimination
        if grille[x1][y1] != 0 or grille[x2][y2] != 0:
            grille[x2][y2] = 0
    
            creation_grille(grille)
            pions_o, pions_x = joueur(grille)
            break

    if destination_totaux_possibles == []:
        print("\nAucun mouvement possible\nChoisir un autre pion ? ou passer son tour ? O / N")
        res = str(input())

        while res != 'o' and res != 'O' and res != 'n' and res != 'N':
            print("Choisir un autre pion ? ou passer son tour ? O / N")
            res = str(input())

        if res == 'o' or res == 'O':
            x1, y1, destination_totaux_possibles = choix_pion_deplacement(grille, tour_o, tour_x)
            deplacement(grille, x1, y1, x2, y2, destination_totaux_possibles, tour_x, tour_o, pions_o, pions_x)

    return grille, pions_o, pions_x


def execution_deplacement(grille, x1, y1, destination_totaux_possibles, tour_x, tour_o):

    #fonction qui execute toutes la prévisualisation des déplacements
    deplacement_haut(x1, y1, grille, destination_totaux_possibles, tour_x, tour_o)
    deplacement_bas(x1, y1, grille, destination_totaux_possibles, tour_x, tour_o)
    deplacement_gauche(x1, y1, grille, destination_totaux_possibles, tour_x, tour_o)
    deplacement_droite(x1, y1, grille, destination_totaux_possibles, tour_x, tour_o)

    diago_haut_gauche(x1, y1, grille, destination_totaux_possibles, tour_x, tour_o)
    diago_haut_droite(x1, y1, grille, destination_totaux_possibles, tour_x, tour_o)
    diago_bas_gauche(x1, y1, grille, destination_totaux_possibles, tour_x, tour_o)
    diago_bas_droite(x1, y1, grille, destination_totaux_possibles, tour_x, tour_o)

    return destination_totaux_possibles

#==============================================================================


#fonction destination qui permet au joueur de rentrer la destination
def fonction_destination(destination_totaux_possibles, x1, y1, grille):
    #on parcourt les éléments (cases possibles) de la liste des déplacements totaux
    case_valide = 0

    while case_valide == 0:
        #avec destination = [x2, y2], x2 et y2 étant le choix du joueur pour la destination
        x2, y2, destination = choix_destination(destination_totaux_possibles)
        #si la case de déplacement correspond a une possibilité de déplacment, on change de place, sinon on resaisie
        for i in range(len(destination_totaux_possibles)):

            if destination == destination_totaux_possibles[i]:
                case_valide += 1
        #changement de place dans la grille si les saisies sont correctes
        if case_valide != 0:
            grille[x1][y1], grille[x2][y2] = grille[x2][y2], grille[x1][y1]
        else:
            print("Case non valide !")

    return grille, x2, y2


def choix_destination(destination_totaux_possibles):

    #on demande de saisir les coordoonées de la destination
    print('\nVeuillez saisir la ligne de la destination (x)')
    x2 = int(input())

    #tant que les coordonnées du pion choisit à déplacer est en dehors de la grille
    while x2 < 0 or x2 > 8:
        print('La ligne choisie est en dehors de la grille,\n' +
              'Veuillez resaisir la ligne du pion à déplacer (x)')
        x2 = int(input())

    print('Veuillez saisir la colonne de la destination (y)')
    y2 = int(input())

    while y2 < 0 or y2 > 8:
        print('La colonne choisie est en dehors de la grille,\n' +
              'Veuillez resaisir la colonne du pion à déplacer (y)')
        y2 = int(input())

    destination = [x2, y2]
    print('Vous avez choisi la destination :', destination)

    return x2, y2, destination


"""   FONCTIONS TOUR DE JEU ET FIN DE JEU   """


def tour_de_jeu(x1, y1, x2, y2, destination_totaux_possibles, un_joueur, deux_joueurs, grille, pions_o, pions_x):

    condition_fin = False
    #le joueur x commence a jouer en premier
    tour_x = True
    tour_o = False

    #tant que la condition de fin est fausse, le jeu continue
    while condition_fin == False:

        #tour du joueur x
        if tour_x:

            print('Au tour du joueur x')
            #on appelle les fonctions deplacement pour choisir et se déplacer
            x1, y1, destination_totaux_possibles = choix_pion_deplacement(grille, tour_o, tour_x)
            deplacement(grille, x1, y1, x2, y2, destination_totaux_possibles, tour_x, tour_o, pions_o, pions_x)

            #on inverse les booléens pour changer de tour après déplacement
            tour_o = True
            tour_x = False
            
            if pions_o < 6 or pions_x < 6:
                condition_fin = True
                fonction_fin(pions_o, pions_x)

        #tour du joueur o
        elif tour_o:
            #si il y a deux joueurs on applique le deplacement classique
            if deux_joueurs:

                print('Au tour du joueur o')
                x1, y1, destination_totaux_possibles = choix_pion_deplacement(grille, tour_o, tour_x)
                deplacement(grille, x1, y1, x2, y2, destination_totaux_possibles, tour_x, tour_o, pions_o, pions_x)

                #on inverse les booléens pour changer de tour
                tour_o = False
                tour_x = True

                if pions_o < 6 or pions_x < 6:
                    condition_fin = True
                    fonction_fin(pions_o, pions_x)

            
            #si il n'y a qu'un joueur, l'ordinateur joue
            elif un_joueur:
                
                print("Au tour de l'ordinateur")

                choix_possible = []
                num_ligne = 0
                #ajout des départs possibles par l'IA en parcourant la liste de la grille
                for ligne in grille:
                    num_colonne = 0

                    for colonne in grille:
                        if grille[num_ligne][num_colonne] == 1:
                            choix_possible.append([num_ligne, num_colonne])

                        num_colonne += 1
                    num_ligne += 1
                
                #l'ordinateur choisi la case du début
                variable_depart = random.randint(0, len(choix_possible)-1)
                depart_random = choix_possible[variable_depart]
                x1, y1 = depart_random[0], depart_random[1]
                print("l'ordinateur a choisi : [",x1, ",", y1,"]")
                
                #appel fonction choix destination et destination par l'IA
                pions_o, pions_x = arrivee_ordinateur(grille, tour_x, tour_o, x1, y1, x2, y2)

                #on inverse les booléens pour changer de tour
                tour_o = False
                tour_x = True

                if pions_o < 6 or pions_x < 6:
                    condition_fin = True
                    fonction_fin(pions_o, pions_x)

    return 0


def arrivee_ordinateur(grille, tour_x, tour_o, x1, y1, x2, y2):

    #choix de la destination par l'IA et on actualise la grille
    destination_totaux_possibles = []
    destination_totaux_possibles = execution_deplacement(grille, x1, y1, destination_totaux_possibles, tour_x, tour_o)

    #on crée une liste avec les destinations possibles et l'IA en choisi une
    if destination_totaux_possibles != []:
        variable_arrivee = random.randint(0, len(destination_totaux_possibles)-1)
        arrivee_random = destination_totaux_possibles[variable_arrivee]
        x2, y2 = arrivee_random[0], arrivee_random[1]

        print("\nl'ordinateur s'est déplacé en : [", arrivee_random[0], ",", arrivee_random[1],"]\n")
        
        #on change les cases pour faire le déplacement du pion
        grille[x1][y1], grille[x2][y2] = grille[x2][y2], grille[x1][y1]

        if grille[x1][y1] != 0:
            grille[x1][y1] = 0

        creation_grille(grille)
        pions_o, pions_x = joueur(grille)

    else:
        print("\nl'ordinateur a sauté son tour")
        creation_grille(grille)
        pions_o, pions_x = joueur(grille)
        
    return pions_o, pions_x


def fonction_fin(pions_o, pions_x):
    #affichage du gagnant si la condition de fin est vrai
    if pions_x > pions_o:  
        print('Fin du jeu, le joueur X a gagné !')

    elif pions_o > pions_x:
        print('Fin du jeu, le joueur O a gagné !')


#fonction qui demande au joueur si il veut jouer à 2 joueurs on contre l'IA
def choix_partie():

    print("Joueur contre joueur ou contre IA ? J / I")
    res = str(input())
    
    while res != 'J' and res != 'j' and res != 'I' and res != 'i':
        print("Joueur contre joueur ou contre IA ? J / I")
        res = str(input())

    if res == 'J' or res == 'j':
        deux_joueurs = True
        un_joueur = False

    elif res == 'I' or res == 'i':
        un_joueur = True
        deux_joueurs = False

    return un_joueur, deux_joueurs

    
"""  MAIN  """

x1,y1,x2,y2 = 0,0,0,0
destination_totaux_possibles = []
un_joueur, deux_joueurs = choix_partie()

grille = type_partie(creation_grille)
pions_o, pions_x = joueur(grille)

#est_dans_grille()

tour_de_jeu(x1, y1, x2, y2, destination_totaux_possibles, un_joueur, deux_joueurs, grille, pions_o, pions_x)