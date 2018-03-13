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
    print('     1   2   3   4   5   6   7   8   9')
    print('   +---+---+---+---+---+---+---+---+---+')

    for ligne in liste_grille:
        print(numero_ligne + 1,' |',end='')
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
def type_partie(debut_partie, milieu_partie, fin_partie):

    print('Debut, Milieu ou Fin de partie ? D / M / F')

    type = str(input())

    if type == 'd' or type == 'D':
        #affichage début de partie
        debut_partie(creation_grille)

    elif type == 'm' or type == 'M':
        #affichage milieu de partie
        milieu_partie(creation_grille)

    elif type == 'f' or type == 'F':
        #affichage fin de partie
        fin_partie(creation_grille)

    #le programme boucle tant que les lettres entrées sont incorrectes
    else:  
        print('Veuillez refaire votre choix')

        type_partie(debut_partie, milieu_partie, fin_partie)


"""  FONCTIONS QUI GERENT LE PLACEMENT DES PIONS EN FONCTION DE LA PARTIE  """

#fonction début de partie qui appelle la fonction de création des pions
def debut_partie(creation_grille):

    liste_grille = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2]]

    return(creation_grille(liste_grille))


#fonction milieu de partie qui appelle la fonction de création des pions
def milieu_partie(creation_grille):

    liste_grille = [[0, 0, 0, 1, 0, 0, 0, 1, 2], 
                    [1, 0, 2, 2, 1, 0, 0, 0, 0], 
                    [2, 1, 1, 0, 0, 0, 0, 0, 1], 
                    [0, 0, 0, 0, 0, 1, 1, 1, 2], 
                    [0, 1, 2, 1, 2, 2, 2, 0, 0], 
                    [0, 2, 1, 0, 1, 2, 1, 0, 0], 
                    [2, 1, 2, 0, 0, 0, 1, 0, 2], 
                    [2, 1, 0, 1, 0, 1, 0, 2, 0], 
                    [0, 0, 1, 0, 2, 0, 1, 0, 1]]

    return(creation_grille(liste_grille))


#fonction fin de partie qui apelle la fonction de création des pions
def fin_partie(creation_grille):

    liste_grille = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 0, 0, 0, 2, 0], 
                    [0, 0, 1, 0, 0, 2, 0 ,0 ,0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 1, 0, 0, 1, 2, 0, 1], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 2, 0, 1, 0, 0], 
                    [1, 0, 0, 0, 1, 2, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    return(creation_grille(liste_grille))


"""  JEUX DE TESTS  """

#saisie de coordonnées pour tester si la case saisie est dans la grille
def est_dans_grille(NB_LIGNE, NB_COLONNE):

    print('"TEST DE COORDONNEES DANS LA GRILLE"')
    print('\nVeuillez saisir le numéro de ligne (la grille va de 1 à 9)')
    ligne = int(input())

    while ligne < 0 or ligne > 9:
        print('La ligne saisie est incorrecte, veuillez la ressaisir')
        ligne = int(input())

    print('Veuillez saisir le numéro de colonne (la grille va de 1 à 9)')
    colonne = int(input())
    
    while colonne < 0 or colonne > 9:
        print('La colonne saisie est incorrecte, veuillez la ressaisir')
        colonne = int(input())
    
    print("\nla case saisie est bien dans la grille")


# à finir
def test_est_dans_grille(est_dans_grille):
    assert est_dans_grille(1,1) == True, "la case demandée n'est pas dans la grille"
    assert est_dans_grille(1,9) == True, "la case demandée n'est pas dans la grille"
    assert est_dans_grille(9,1) == True, "la case demandée n'est pas dans la grille"
    assert est_dans_grille(9,9) == True, "la case demandée n'est pas dans la grille"
    #assert est_dans_grille(10,23) == True, "la case demandée n'est pas dans la grille"


"""  MAIN  """

type_partie(debut_partie, milieu_partie, fin_partie)
joueur(PIONS_O, PIONS_X)

est_dans_grille(NB_LIGNE, NB_COLONNE)
#test_est_dans_grille(est_dans_grille)