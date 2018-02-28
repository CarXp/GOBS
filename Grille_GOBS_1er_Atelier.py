# ======================================================================================================================
#             _____  ____  ____   _____   _______     _________ _    _  ____  _   _   
#            / ____|/ __ \|  _ \ / ____| |  __ \ \   / /__   __| |  | |/ __ \| \ | |
#           | |  __| |  | | |_) | (___   | |__) \ \_/ /   | |  | |__| | |  | |  \| |
#           | | |_ | |  | |  _ < \___ \  |  ___/ \   /    | |  |  __  | |  | | . ` |
#           | |__| | |__| | |_) |____) | | |      | |     | |  | |  | | |__| | |\  |
#            \_____|\____/|____/|_____/  |_|      |_|     |_|  |_|  |_|\____/|_| \_|
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
# _______________________________________________________________________________________________________________________


from tkinter import*


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

"""  FONCTIONS INTERFACES  """

#fonction qui crée l'interface du début de jeu
def interface(fenetre, creation_grille, joueur):
    #cadre 1 pour le haut de la fenetre
    cadre1 = Frame(fenetre, width=470, height=50, bg='#808080', borderwidth=3, pady = 2)
    cadre1.pack()

    #cadre 2 pour la grille
    cadre2 = Frame(fenetre, width=452, height=450, bg='#101010', borderwidth=7)
    cadre2.pack()

    #cadre 3 et 4 pour le bas de la fenetre
    cadre3 = Frame(fenetre, width=235, height=45, bg='#101010', borderwidth=2)
    cadre3.pack(side=LEFT, padx = 40)
    
    cadre4 = Frame(fenetre, width=235, height=45, bg='#101010', borderwidth=2)
    cadre4.pack(side=RIGHT, padx = 40)

    #creation de la grille avec l'outil Canvas
    grille = Canvas(cadre2, width=450, height=450, bg='#101010', borderwidth=1)
    grille.pack()

    # fonction grille
    creation_grille(grille, fenetre, CASE, NB_COLONNE, NB_LIGNE)

    #affichage de "joueur 1" et "joueur 2"
    joueur(cadre3, cadre4)

    type_partie(cadre1, grille, debut_partie, milieu_partie, fin_partie)


#fonction création des labels "joueur 1" et "joueur 2"
def joueur(cadre3, cadre4):

    label_joueur1 = Label(cadre3, text = 'JOUEUR 1 : ROUGE', font='Calibri 12', 
    relief='ridge', bg = '#101010', fg = '#ED0000', padx = 2, pady = 5, borderwidth = 3)
    label_joueur1.pack()

    label_joueur2 = Label(cadre4, text= 'JOUEUR 2 : BLEU', font='Calibri 12',
     relief='ridge', bg = '#101010', fg = '#00CCCB', padx = 10, pady = 5, borderwidth = 3)
    label_joueur2.pack()


#on définie la fonction qui va créer la grille
def creation_grille(grille, cadre2, CASE, NB_COLONNE, NB_LIGNE):
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


"""  MAIN  """

#création de la fenetre
fenetre = Tk()
fenetre.title('GOBS Python')
fenetre['bg']='#101010'
fenetre.resizable(False, False)

#lancement de l'interface de jeu et du jeu de test de la grille
interface(fenetre, creation_grille, joueur)

est_dans_grille(NB_COLONNE, NB_LIGNE)

fenetre.mainloop()