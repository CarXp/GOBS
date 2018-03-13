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
#       - CONSTANTES
#       - FONCTIONS INTERFACE
#       - FONCTION QUI GERE LA CREATION DES PIONS
#       - FONCTIONS QUI GERENT LA CREATION DES PIONS
#       - JEUX DE TESTS
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
                                                             
#import test_deplacement_GOBS


"""  CONSTANTES  """

#nombre de lignes et de colonne dans la grille
NB_LIGNE = 9
NB_COLONNE = 9

PIONS_O = 27
PIONS_X = 27


"""  FONCTIONS INTERFACES  """

#affichage de "joueur 1 : O" et "joueur 2 : X"
def joueur(PIONS_O, PIONS_X):
    print('    Joueur O :', PIONS_O ,'      Joueur X : ',PIONS_X)
    print('')


#on définie la fonction qui va créer la grille
def creation_grille(liste_grille):
    numero_ligne = 0
    print('     0   1   2   3   4   5   6   7   8')
    print('   +---+---+---+---+---+---+---+---+---+')

    for ligne in liste_grille:
        print(numero_ligne,' |',end='')
        numero_colonne = 0

        for colonne in ligne:
            if numero_colonne < 8:
                if liste_grille[numero_ligne][numero_colonne]==0:
                    print('   |',end='')
                elif liste_grille[numero_ligne][numero_colonne]==1:
                    print(' O |',end='')
                elif liste_grille[numero_ligne][numero_colonne]==2:
                    print(' X |',end='')

            else:
                if liste_grille[numero_ligne][numero_colonne]==0:
                    print('   |')
                elif liste_grille[numero_ligne][numero_colonne]==1:
                    print(' O |')
                elif liste_grille[numero_ligne][numero_colonne]==2:
                    print(' X |')

                print('   +---+---+---+---+---+---+---+---+---+')
            numero_colonne = numero_colonne + 1
        numero_ligne = numero_ligne + 1


#fonction qui demande au joueur la configuration voulue
def type_partie():

    print('Debut, Milieu ou Fin de partie ? D / M / F')

    type = str(input())

    if type == 'd' or type == 'D':
        #affichage début de partie
        liste_grille = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [2, 2, 2, 2, 2, 2, 2, 2, 2],
                        [2, 2, 2, 2, 2, 2, 2, 2, 2],
                        [2, 2, 2, 2, 2, 2, 2, 2, 2]]

        creation_grille(liste_grille)
        return liste_grille

    elif type == 'm' or type == 'M':
        #affichage milieu de partie
        liste_grille = [[0, 0, 0, 1, 0, 0, 0, 1, 2], 
                        [1, 0, 2, 2, 1, 0, 0, 0, 0], 
                        [2, 1, 1, 0, 0, 0, 0, 0, 1], 
                        [0, 0, 0, 0, 0, 1, 1, 1, 2], 
                        [0, 1, 2, 1, 2, 2, 2, 0, 0], 
                        [0, 2, 1, 0, 1, 2, 1, 0, 0], 
                        [2, 1, 2, 0, 0, 0, 1, 0, 2], 
                        [2, 1, 0, 1, 0, 1, 0, 2, 0], 
                        [0, 0, 1, 0, 2, 0, 1, 0, 1]]

        creation_grille(liste_grille)
        return liste_grille

    elif type == 'f' or type == 'F':
        #affichage fin de partie
        liste_grille = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 1, 0, 0, 0, 2, 0], 
                        [0, 0, 1, 0, 0, 2, 0 ,0 ,0], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 1, 0, 0, 1, 2, 0, 1], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 2, 0, 1, 0, 0], 
                        [1, 0, 0, 0, 1, 2, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        creation_grille(liste_grille)
        return liste_grille

    #le programme boucle tant que les lettres entrées sont incorrectes
    else:  
        print('Veuillez refaire votre choix')

        type_partie()


"""  JEUX DE TESTS  """

#à changer
#saisie de coordonnées pour tester si la case saisie est dans la grille
def est_dans_grille(NB_LIGNE, NB_COLONNE):

    print('"""  TEST DE COORDONNEES DANS LA GRILLE  ""')
    print('\nVeuillez saisir le numéro de ligne (la grille va de 0 à 8)')
    ligne = int(input())

    print('Veuillez saisir le numéro de colonne (la grille va de 0 à 8)')
    colonne = int(input())
    
    if ligne < 0 or ligne > 8 or colonne < 0 or colonne > 8:
        print("\nla case saisie n'est pas dans la grille\n")
    else:
        print("\nla case saisie est bien dans la grille\n")


# à finir
def test_est_dans_grille(est_dans_grille):
    assert est_dans_grille(1,1) == True, "la case demandée n'est pas dans la grille"
    assert est_dans_grille(1,9) == True, "la case demandée n'est pas dans la grille"
    assert est_dans_grille(9,1) == True, "la case demandée n'est pas dans la grille"
    assert est_dans_grille(9,9) == True, "la case demandée n'est pas dans la grille"
    #assert est_dans_grille(10,23) == True, "la case demandée n'est pas dans la grille"


# =======================================================================================================================
#                 ____             _                                     _       
#                |  _ \  ___ _ __ | | __ _  ___ ___ _ __ ___   ___ _ __ | |_ ___ 
#                | | | |/ _ \ '_ \| |/ _` |/ __/ _ \ '_ ` _ \ / _ \ '_ \| __/ __|
#                | |_| |  __/ |_) | | (_| | (_|  __/ | | | | |  __/ | | | |_\__ \
#                |____/ \___| .__/|_|\__,_|\___\___|_| |_| |_|\___|_| |_|\__|___/
#                           |_|                                                  
# =======================================================================================================================

"""  FONCTIONS DEPLACEMENTS DROITES  """

#fonction déplacement du pion bleu
def deplacement_bleu(obstacle, tour, liste_grille):

    #tant qu'on peut déplacer le pion bleu
    while deplacement_bleu:

        #choix de la ligne du pion voulu
        print('Choisissez le pion bleu à déplacer, (ligne/colonne)')
        print('ligne : ')
        ligne_choisi = int(input())

        #si le choix est en dehors de la grille, le joueur rechoisit
        if ligne_choisi < 0 or ligne_choisi > 9:
            print('veuillez rechoisir le pion bleu')
            deplacement_bleu(obstacle, tour, liste_grille)
        
        print('colonne : ')
        colonne_choisi = int(input())
        
        #si le choix est en dehors de la grille, le joueur rechoisit
        if colonne_choisi < 0 or colonne_choisi > 9:
            print('veuillez rechoisir le pion bleu')
            deplacement_bleu(obstacle, tour, liste_grille)
    
        pion_choisi = (ligne_choisi, colonne_choisi)

        #appel des fonctions déplacements
        deplacement_haut(pion_choisi, obstacle, tour, liste_grille)
        deplacement_bas(pion_choisi, obstacle, tour, liste_grille)
        deplacement_gauche(pion_choisi, obstacle, tour, liste_grille)
        deplacement_droite(pion_choisi, obstacle, tour, liste_grille)

    deplacement_bleu == False


#fonction déplacement vers le haut
def deplacement_haut(ligne_choisi, colonne_choisi, liste_grille):

    deplacement_haut_possible = 0
    case_suivante = 1
    obstacle = False

    #tant que le deplacement vers le haut n'est pas gêné par un obstacle
    while obstacle == False and ligne_choisi-case_suivante >= 0:
        #si la case possible est 0, on peut se déplacer
        if liste_grille[ligne_choisi-case_suivante][colonne_choisi] == 0:
            deplacement_haut_possible += 1
        #sinon, on est bloqué par un obstacle
        else:
            obstacle = True
        #on actualise la case à traiter
        case_suivante = case_suivante+1

    print('\nDeplacement possible de', deplacement_haut_possible, 'cases vers le haut')
    return deplacement_haut_possible
    

#fonction déplacement vers le bas
def deplacement_bas(ligne_choisi, colonne_choisi, liste_grille):

    deplacement_bas_possible = 0
    case_suivante = 1
    obstacle = False

    #tant que le deplacement vers le bas n'est pas gêné par un obstacle
    while obstacle == False and ligne_choisi+case_suivante <= 8:
        #si la case possible est 0, on peut se déplacer
        if liste_grille[ligne_choisi+case_suivante][colonne_choisi] == 0:
            deplacement_bas_possible += 1
        #sinon, on est bloqué par un obstacle
        else:
            obstacle = True
        #on actualise la case à traiter
        case_suivante = case_suivante+1

    print('Deplacement possible de', deplacement_bas_possible, 'cases vers le bas')
    return deplacement_bas_possible


#fonction déplacement vers la gauche
def deplacement_gauche(ligne_choisi, colonne_choisi, liste_grille):

    deplacement_gauche_possible = 0
    case_suivante = 1
    obstacle = False
    
    #tant que le deplacement vers la gauche n'est pas gêné par un obstacle
    while obstacle == False and colonne_choisi-case_suivante >= 0:
        #si la case possible est 0, on peut se déplacer
        if liste_grille[ligne_choisi][colonne_choisi-case_suivante] == 0:
            deplacement_gauche_possible += 1
        #sinon, on est bloqué par un obstacle
        else:
            obstacle = True
        #on actualise la case à traiter
        case_suivante = case_suivante+1

    print('Deplacement possible de', deplacement_gauche_possible, 'cases vers la gauche')
    return deplacement_gauche_possible


#fonction déplacement vers la droite
def deplacement_droite(ligne_choisi, colonne_choisi, liste_grille):

    deplacement_droite_possible = 0
    case_suivante = 1
    obstacle = False

    #tant que le deplacement vers la droite n'est pas gêné par un obstacle
    while obstacle == False and colonne_choisi+case_suivante <= 8:
        #si la case possible est 0, on peut se déplacer
        if liste_grille[ligne_choisi][colonne_choisi+case_suivante] == 0:
            deplacement_droite_possible += 1
        #sinon, on est bloqué par un obstacle
        else:
            obstacle = True
        #on actualise la case à traiter
        case_suivante = case_suivante+1

    print('Deplacement possible de', deplacement_droite_possible, 'cases vers la droite')
    return deplacement_droite_possible


"""  FONCTIONS DEPLACEMENTS DIAGONALES  """

#==============================================================================

def bordure(pion_choisi):

    #limitation des bordures de la grille aux 2 cases côtés extérieur dans la grille
    bordure_haut = False
    bordure_bas = False
    bordure_gauche = False
    bordure_droite = False

    if pion_choisi[0] == 1 or pion_choisi[0] == 2:
        bordure_haut = True
    
    if pion_choisi[0] == 8 or pion_choisi[0] == 9:
        bordure_bas = True

    if pion_choisi[1] == 1 or pion_choisi[1] == 2:
        bordure_gauche = True

    if pion_choisi[1] == 8 or pion_choisi[1] == 9:
        bordure_droite = True

    print(bordure_haut, bordure_bas, bordure_gauche, bordure_droite)
    return(bordure_haut, bordure_bas, bordure_gauche, bordure_droite)


#mettre dans le 2eme fichier
def test_fin_jeu(deplacement_bleu, deplacement_rouge):
    
    if PIONS_O < 6 and deplacement_bleu == False:
        print('Le Joueur rouge a gagné !')

    elif PIONS_X < 6 and deplacement_rouge == False:
        print('Le Joueur bleu a gagné !')



def tour_de_jeu(test_fin_jeu, deplacement_rouge, deplacement_bleu):

    tour = 0
    while test_fin_jeu() == False: #tant que la condition de fin de partie est fausse
        
        print('voulez vous jouer ou passer votre tour ? J / P')
        
        choix = str(input())

        #si le tour est pair, le joueur rouge joue, sinon le joueur bleu joue
        if choix == 'j' or choix == 'J':
            if tour % 2 == 0:
                print('Au tour du joueur rouge')
                deplacement_rouge()
        
            else:
                print('Au tour du joueur bleu')
                deplacement_bleu()
            tour = tour+1
            tour_de_jeu(test_fin_jeu, deplacement_rouge, deplacement_bleu)

        elif choix == 'p' or choix == 'p':
            tour = tour+1
            tour_de_jeu(test_fin_jeu, deplacement_rouge, deplacement_bleu)

        else:
            print('veuillez refaire votre choix')
            tour_de_jeu(test_fin_jeu, deplacement_rouge, deplacement_bleu)


def pion_incorrect(ligne_choisi, colonne_choisi, liste_grille):
    #tant que l'utilisateur ne choisi pas un pion, redemander de saisir
    while liste_grille[ligne_choisi][colonne_choisi] == 0:
        print('Choix du pion invalide !')
        print('Veuillez resaisir la ligne du pion à déplacer')
        ligne_choisi = int(input())

        while ligne_choisi < 0 or ligne_choisi > 8:
            print('Veuillez resaisir la ligne du pion à déplacer')
            ligne_choisi = int(input())

        print('Veuillez resaisir la colonne du pion à déplacer')
        colonne_choisi = int(input())

        while colonne_choisi < 0 or colonne_choisi > 8:
            print('Veuillez resaisir la colonne du pion à déplacer')
            colonne_choisi = int(input())


"""  MAIN  """

liste_grille = type_partie()
joueur(PIONS_O, PIONS_X)


est_dans_grille(NB_LIGNE, NB_COLONNE)
#test_est_dans_grille(est_dans_grille)

print('"""  DEPLACEMENT PIONS  """')
print('veuillez saisir la ligne du pion à déplacer')
ligne_choisi = int(input())

while ligne_choisi < 0 or ligne_choisi > 8:
    print('La ligne choisie est en dehors de la grille,\n'
    +'Veuillez resaisir la ligne du pion à déplacer')
    ligne_choisi = int(input())

print('Veuillez saisir la colonne du pion à déplacer')
colonne_choisi = int(input())

while colonne_choisi < 0 or colonne_choisi > 8:
    print('La colonne choisie est en dehors de la grille,\n'
    +'Veuillez resaisir la colonne du pion à déplacer')
    colonne_choisi = int(input())

pion_choisi = (ligne_choisi, colonne_choisi)
print('Vous avez choisi le pion en : (',ligne_choisi,',', colonne_choisi,')')

bordure(pion_choisi)
pion_incorrect(ligne_choisi, colonne_choisi, liste_grille)

deplacement_haut(ligne_choisi, colonne_choisi, liste_grille)
deplacement_bas(ligne_choisi, colonne_choisi, liste_grille)
deplacement_gauche(ligne_choisi, colonne_choisi, liste_grille)
deplacement_droite(ligne_choisi, colonne_choisi, liste_grille)