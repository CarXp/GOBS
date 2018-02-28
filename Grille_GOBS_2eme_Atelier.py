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
# _______________________________________________________________________________________________________________________
#
#   Ce programme utilise des fonctionnalités d'une bibliothèque intégré à Python qui s'apelle "tkinter". 
#   Il vous faut donc avoir Python d'installé sur votre PC pour pouvoir exécuter le programme 
#   Veuillez donc tout d'abord vous assurer d'avoir téléchargé la dernière version de PYTHON 3.6 sur son site officiel.
# 
# =======================================================================================================================
#
#            _____ _   _ _______ ______ _____  ______      _____ ______ 
#           |_   _| \ | |__   __|  ____|  __ \|  ____/\   / ____|  ____|
#             | | |  \| |  | |  | |__  | |__) | |__ /  \ | |    | |__   
#             | | | . ` |  | |  |  __| |  _  /|  __/ /\ \| |    |  __|  
#            _| |_| |\  |  | |  | |____| | \ \| | / ____ \ |____| |____ 
#           |_____|_| \_|  |_|  |______|_|  \_\_|/_/    \_\_____|______|
#
# =======================================================================================================================
                                                             
from tkinter import*
#import test_deplacement_GOBS


"""  CONSTANTES  """

#la longueur d'une case en pixel
CASE = 50

#coordonnés circulaires pour un pion, XO et YO réprésentant les coordonnées du coin 
#supérieur gauche et X1 et Y1 les coordonnées du coin inférieur droit
X0,X1 = 15,35
Y0,Y1 = 15,35

#nombre de lignes et de colonne dans la grille
NB_LIGNE = 9
NB_COLONNE = 9

PIONS_ROUGES = 27
PIONS_BLEUS = 27

"""  FONCTIONS INTERFACES  """

#fonction qui crée l'interface du début de jeu
def interface(fenetre, creation_grille, joueur):
    #cadre 1 pour le haut de la fenetre
    cadre1 = Frame(fenetre, width=500, height=50, bg='#808080', borderwidth=3, pady = 2)
    cadre1.pack()

    #cadre 2 pour la grille
    cadre2 = Frame(fenetre, width=452, height=450, bg='#101010', borderwidth=7)
    cadre2.pack()  

    cadre_ligne = Frame(cadre2, width=450, height=35, padx = 1, pady = 1)
    cadre_ligne.pack()

    cadre_colonne = Frame(cadre2, width = 30, height = 450)
    cadre_colonne.pack(side=LEFT)

    #cadre 3 et 4 pour le bas de la fenetre
    cadre3 = Frame(fenetre, width=235, height=45, bg='#101010', borderwidth=2)
    cadre3.pack(side=LEFT, padx = 40)
    
    cadre4 = Frame(fenetre, width=235, height=45, bg='#101010', borderwidth=2)
    cadre4.pack(side=RIGHT, padx = 40)

    #creation de la grille avec l'outil Canvas
    grille = Canvas(cadre2, width=450, height=450, bg='#101010', borderwidth=1)
    grille.pack()

    # fonction grille
    creation_grille(grille, cadre2, CASE, NB_COLONNE, NB_LIGNE, cadre_ligne, cadre_colonne)

    #affichage de "joueur 1" et "joueur 2"
    joueur(cadre3, cadre4)

    type_partie(cadre1, grille, debut_partie, milieu_partie, fin_partie)


#fonction création des labels "joueur 1" et "joueur 2"
def joueur(cadre3, cadre4):

    label_joueur1 = Label(cadre3, text = 'JOUEUR 1 : ROUGE', font='Calibri 12', 
    relief='ridge', bg = '#101010', fg = '#ED0000', padx = 2, pady = 5, borderwidth = 3)
    label_joueur1.pack()

    label_joueur2 = Label(cadre4, text  = 'JOUEUR 2 : BLEU', font='Calibri 12',
     relief='ridge', bg = '#101010', fg = '#00CCCB', padx = 10, pady = 5, borderwidth = 3)
    label_joueur2.pack()


#on définie la fonction qui va créer la grille
def creation_grille(grille, cadre2, CASE, NB_COLONNE, NB_LIGNE, cadre_ligne, cadre_colonne):
    #création de la grille sur l'axe horizontal
    for ligne in range(NB_LIGNE):
        #création de la grille sur l'axe vertical
        for colonne in range(NB_COLONNE):
            #attribution de la couleur de la case après sa création
            #si case paire, la case est grise
            if (ligne+colonne)%2 == 0:
                grille.create_rectangle(colonne*CASE, ligne*CASE, 
                (colonne+1)*CASE, (ligne+1)*CASE, fill='#7F7F7F')
            #sinon, la case est noire
            else:
                grille.create_rectangle(colonne*CASE, ligne*CASE, 
                (colonne+1)*CASE, (ligne+1)*CASE, fill='#101010')
    
    #création de l'affichage de lignes et colonnes
    label_ligne = Label(cadre_ligne, text = '      1                2                3\
            4               5               6               7               8\
                9', bg = '#CECECE', width = 60, height = 1, padx = 30, pady = 4)
    label_ligne.pack()
    
    for colonne in range(NB_COLONNE):

        label_colonne = Label(cadre_colonne, text = colonne+1, width = 3,
        height = 3, padx = 1, pady = 1, bg='#CECECE')
        label_colonne.pack()

#fonction qui demande à l'utilisateur le configuration de partie demandée
def type_partie(cadre1, grille, debut_partie, milieu_partie, fin_partie):

    print('Debut, Milieu ou Fin de partie ? D / M / F')

    type = str(input())

    if type == 'd' or type == 'D':
        #affichage début de partie
        debut_partie(cadre1, grille, fenetre, creation_pions)

    elif type == 'm' or type == 'M':
        #affichage milieu de partie
        milieu_partie(cadre1, grille, fenetre, creation_pions)

    elif type == 'f' or type == 'F':
        #affichage fin de partie
        fin_partie(cadre1, grille, fenetre, creation_pions)

    else:
        label_titre = Label(cadre1, text = 'ERREUR CHOIX', bg = '#404040', 
        fg = 'white', padx = 15, pady = 5, borderwidth = 2)
        label_titre.pack()
        
        print('Veuillez refaire votre choix')
        
        type_partie(cadre1, grille, debut_partie, milieu_partie, fin_partie)


"""  FONCTION QUI GERE LA CREATION DES PIONS  """

#fonction création des pions de la grille en fonction de la liste_grille
def creation_pions(liste_grille, grille, CASE):
    
    num_ligne=0
    #liste_grille représente la liste de la grille, on parcours donc les lignes de la grille
    for ligne in liste_grille:
        num_colonne=0
        #on parcours ensuite la liste pour les lignes
        for colonne in ligne:
            #si le numéro de la colonne est 1, on crée un pion rouge, si le numéro est 2, on créée un pion bleu
            if colonne == 1:
                grille.create_oval(X0+CASE*num_colonne,Y0+(CASE*num_ligne),
                X1+CASE*num_colonne,Y1+(CASE*num_ligne), fill='#FF5E4D')

            elif colonne == 2:
                grille.create_oval(X0+CASE*num_colonne,Y0+(CASE*num_ligne),
                X1+CASE*num_colonne,Y1+(CASE*num_ligne), fill='#00CCCB')

            num_colonne = num_colonne+1
        num_ligne=num_ligne+1


"""  FONCTIONS QUI GERENT LE PLACEMENT DES PIONS EN FONCTION DE LA PARTIE  """

#fonction début de partie qui appelle la fonction de création des pions
def debut_partie(cadre1, grille, fenetre, creation_pions):

    label_titre = Label(cadre1, text = 'GOBS DEBUT DE PARTIE', 
    bg = '#404040', fg = 'white', padx = 15, pady = 5, borderwidth = 2)
    label_titre.pack()

    liste_grille = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2]]

    creation_pions(liste_grille, grille, CASE)


#fonction milieu de partie qui appelle la fonction de création des pions
def milieu_partie(cadre1, grille, fenetre, creation_pions):

    label_titre = Label(cadre1, text = 'GOBS MILIEU DE PARTIE', 
    bg = '#404040', fg = 'white', padx = 15, pady = 5, borderwidth = 2)
    label_titre.pack()

    liste_grille = [[0, 0, 0, 1, 0, 0, 0, 1, 2], 
                    [1, 0, 2, 2, 1, 0, 0, 0, 0], 
                    [2, 1, 1, 0, 0, 0, 0, 0, 1], 
                    [0, 0, 0, 0, 0, 1, 1, 1, 2], 
                    [0, 1, 2, 1, 2, 2, 2, 0, 0], 
                    [0, 2, 1, 0, 1, 2, 1, 0, 0], 
                    [2, 1, 2, 0, 0, 0, 1, 0, 2], 
                    [2, 1, 0, 1, 0, 1, 0, 2, 0], 
                    [0, 0, 1, 0, 2, 0, 1, 0, 1]]

    creation_pions(liste_grille, grille, CASE)


#fonction fin de partie qui apelle la fonction de création des pions
def fin_partie(cadre1, grille, fenetre, creation_pions):

    label_titre = Label(cadre1, text = 'GOBS FIN DE PARTIE', 
    bg = '#404040', fg = 'white', padx = 15, pady = 5, borderwidth = 2)
    label_titre.pack()

    liste_grille = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 0, 0, 0, 2, 0], 
                    [0, 0, 1, 0, 0, 2, 0 ,0 ,0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 1, 0, 0, 1, 2, 0, 1], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 2, 0, 1, 0, 0], 
                    [1, 0, 0, 0, 1, 2, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    creation_pions(liste_grille, grille, CASE)


"""  JEUX DE TESTS  """

#saisie de coordonnées pour tester si la case saisie est dans la grille
def est_dans_grille(NB_COLONNE, NB_LIGNE):

    print('"TEST DE COORDONNEES DANS LA GRILLE"')
    print('Veuillez saisir le numéro de ligne (la grille va de 1 à 9)')
    ligne = int(input())

    print('Veuillez saisir le numéro de colonne (la grille va de 1 à 9)')
    colonne = int(input())

    assert 0 < ligne <= NB_LIGNE and 0 < colonne <= NB_COLONNE, "ERREUR COORDONNEES,\
    les coordonnées saisies ne sont pas dans la grille"
    
    print("la case saisie est bien dans la grille")

""" A REVOIR 

def test_est_dans_grille(est_dans_grille):
    assert est_dans_grille(1,1) == TRUE, "la case demandée n'est pas dans la grille"
    assert est_dans_grille(1,9) == TRUE, "la case demandée n'est pas dans la grille"
    assert est_dans_grille(9,1) == TRUE, "la case demandée n'est pas dans la grille"
    assert est_dans_grille(9,9) == TRUE, "la case demandée n'est pas dans la grille"
    #assert est_dans_grille(10,23) == TRUE, "la case demandée n'est pas dans la grille"
"""

# =======================================================================================================================
#
#            _____  ______ _____  _               _____ ______ __  __ ______ _   _ _______ _____ 
#           |  __ \|  ____|  __ \| |        /\   / ____|  ____|  \/  |  ____| \ | |__   __/ ____|
#           | |  | | |__  | |__) | |       /  \ | |    | |__  | \  / | |__  |  \| |  | | | (___  
#           | |  | |  __| |  ___/| |      / /\ \| |    |  __| | |\/| |  __| | . ` |  | |  \___ \ 
#           | |__| | |____| |    | |____ / ____ \ |____| |____| |  | | |____| |\  |  | |  ____) |
#           |_____/|______|_|    |______/_/    \_\_____|______|_|  |_|______|_| \_|  |_| |_____/ 
#
# =======================================================================================================================

"""  FONCTIONS DEPLACEMENTS  """

#demander a dylan pour verifier le type 'int'
def deplacement_rouge():

    deplacement_rouge = FALSE

    while deplacement_rouge == TRUE:

        print('Choisissez le pion rouge à déplacer, (ligne/colonne)')
        print('ligne : ')
        ligne_choisi = int(input())

        if ligne_choisi < 0 and ligne_choisi > 9:
            print('veuillez rechoisir le pion rouge')
            deplacement_rouge()
        
        print('colonne : ')
        colonne_choisi = int(input())

        if colonne_choisi < 0 and colonne_choisi > 9:
            print('veuillez rechoisir le pion rouge')
            deplacement_rouge()
    
    deplacement_rouge == FALSE


def deplacement_bleu():

    deplacement_bleu = FALSE

    while deplacement_bleu == TRUE:

        print('Choisissez le pion bleu à déplacer, (ligne/colonne)')
        print('ligne : ')
        ligne_choisi = int(input())

        if ligne_choisi < 0 and ligne_choisi > 9:
            print('veuillez rechoisir le pion bleu')
            deplacement_bleu()
        
        print('colonne : ')
        colonne_choisi = int(input())

        if colonne_choisi < 0 and colonne_choisi > 9:
            print('veuillez rechoisir le pion bleu')
            deplacement_bleu()

    deplacement_bleu == FALSE


#fonction déplacement vers le haut
def deplacement_haut(obstacle, tour_de_jeu):

    deplacement_haut_possible = []
    case_suivante = 1
    obstacle = FALSE

    #si le tour est pair, le joueur 1 (rouge) joue
    if tour % 2 == 0:
        #tant que le deplacement vers le haut n'est pas gêné par un obstacle
        while obstacle == FALSE:
            #si la case possible est 0, on peut se déplacer
            if case_possible == 0:
                deplacement_haut_possible.append[1]
            #sinon, on est bloqué par un obstacle
            else:
                obstacle = TRUE
            #on actualise la case à traiter
            case_suivante = case_suivante+1

    #si le tour est impair, le joueur 2 (bleu) joue
    elif tour % 2 != 0:
        #tant que non gêné
        while obstacle == FALSE:
            #si case = 0, déplacement possible
            if case_possible == 0:
                deplacement_haut_possible.append[2]
            #sinon, bloqué
            else:
                obstacle == TRUE
            case_suivante = case_suivante+1
    
    return deplacement_haut_possible


#meme fonction pour le deplacement vers le bas
def deplacement_bas(obstacle, tour_de_jeu):

    deplacement_haut_possible = []
    case_suivante = 1
    obstacle = FALSE

    #si le tour est pair, le joueur 1 (rouge) joue
    if tour % 2 == 0:
        while obstacle == FALSE:
            #si la case possible est 0, on peut se déplacer
            if case_possible == 0:
                deplacement_bas_possible.append[1]
            #sinon, on est bloqué par un obstacle
            else:
                obstacle = TRUE
            #on actualise la case à traiter
            case_suivante = case_suivante+1

    #si le tour est pair, le joueur 2 (bleu) joue
    elif tour % 2 != 0:
        while obstacle == FALSE:
            #si case = 0, déplacement possible
            if case_possible == 0:
                deplacement_bas_possible.append[2]
            #sinon, bloqué
            else:
                obstacle == TRUE
            case_suivante = case_suivante+1

    return deplacement_bas_possible

#meme fonction pour le deplacement vers la gauche
def deplacement_gauche(obstacle, tour_de_jeu):

    deplacement_gauche_possible = []
    case_suivante = 1
    obstacle = FALSE

    #si le tour est pair, le joueur 1 (rouge) joue
    if tour % 2 == 0:
        while obstacle == FALSE:
            #si la case possible est 0, on peut se déplacer
            if case_possible == 0:
                deplacement_gauche_possible.append[1]
            #sinon, on est bloqué par un obstacle
            else:
                obstacle = TRUE
            #on actualise la case à traiter
            case_suivante = case_suivante+1

    #si le tour est pair, le joueur 2 (bleu) joue
    elif tour % 2 != 0:
        while obstacle == FALSE:
            #si case = 0, déplacement possible
            if case_possible == 0:
                deplacement_gauche_possible.append[2]
            #sinon, bloqué
            else:
                obstacle == TRUE
            case_suivante = case_suivante+1

    return deplacement_gauche_possible

#meme fonction pour le deplacement vers la droite
def deplacement_droite(obstacle, tour_de_jeu):
    
    deplacement_droite_possible = []
    case_suivante = 1
    obstacle = FALSE

    #si le tour est pair, le joueur 1 (rouge) joue
    if tour % 2 == 0:
        while obstacle == FALSE:
            #si la case possible est 0, on peut se déplacer
            if case_possible == 0:
                deplacement_droite_possible.append[1]
            #sinon, on est bloqué par un obstacle
            else:
                obstacle = TRUE
            #on actualise la case à traiter
            case_suivante = case_suivante+1

    #si le tour est pair, le joueur 2 (bleu) joue
    elif tour % 2 != 0:
        while obstacle == FALSE:
            #si case = 0, déplacement possible
            if case_possible == 0:
                deplacement_droite_possible.append[2]
            #sinon, bloqué
            else:
                obstacle == TRUE
            case_suivante = case_suivante+1

    return deplacement_droite_possible


#mettre dans le 2eme fichier
def test_fin_jeu(deplacement_bleu, deplacement_rouge):
    
    if PIONS_BLEUS < 6 and deplacement_bleu == FALSE:
        print('Le Joueur rouge a gagné !')

    elif PIONS_ROUGES < 6 and deplacement_rouge == FALSE:
        print('Le Joueur bleu a gagné !')



def tour_de_jeu(test_fin_jeu, deplacement_rouge, deplacement_bleu):
    
    while test_fin_jeu() == FALSE: #tant que la condition de fin de partie est fausse
        tour = 0

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



"""  MAIN  """

#création de la fenetre
fenetre = Tk()
fenetre.title('GOBS Python')
fenetre['bg']='#101010'
fenetre.resizable(False, False)

#lancement de l'interface de jeu et du jeu de test de la grille
interface(fenetre, creation_grille, joueur)

est_dans_grille(NB_COLONNE, NB_LIGNE)

#test_est_dans_grille(est_dans_grille)

#tour_de_jeu(test_fin_jeu, deplacement_rouge, deplacement_bleu)

fenetre.mainloop()