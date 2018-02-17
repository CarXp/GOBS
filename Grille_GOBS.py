""" 
Si vous n'arrivez pas à lancer le programme, veuillez tout d'abord télécharger la dernière version de PYTHON 3.6 sur son site officiel. 
Ce programme utilise des fonctionnalités d'une bibliothèque intégré à Python qui s'apelle "tkinter". Il vous faut donc Python sur votre PC pour pouvoir exécuter le programme 

"""

from tkinter import*


"""  CONSTANTES  """

#la longueur d'une case en pixel
CASE = 50

#coordonnés circulaires pour un pion, XO et YO réprésentant les coordonnées du coin supérieur gauche et X1 et Y1 les coordonnées du coin inférieur droit
X0,X1 = 15,35
Y0,Y1 = 15,35


"""  FONCTIONS  """

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
    creation_grille(grille, fenetre, CASE)

    #affichage de "joueur 1" et "joueur 2"
    joueur(cadre3, cadre4)

    type_partie(cadre1, grille, debut_partie, milieu_partie, fin_partie)


#fonction création des labels "joueur 1" et "joueur 2"
def joueur(cadre3, cadre4):

    label_joueur1 = Label(cadre3, text = 'JOUEUR 1 : ROUGE', font='Calibri 12', relief='ridge', bg = '#101010', fg = '#ED0000', padx = 2, pady = 5, borderwidth = 3)
    label_joueur1.pack()

    label_joueur2 = Label(cadre4, text= 'JOUEUR 2 : BLEU', font='Calibri 12', relief='ridge', bg = '#101010', fg = '#00CCCB', padx = 10, pady = 5, borderwidth = 3)
    label_joueur2.pack()


#on définie la fonction qui va créer la grille
def creation_grille(grille, cadre2, CASE):
    #création de la grille sur l'axe horizontal
    for ligne in range(9):
        #création de la grille sur l'axe vertical
        for colonne in range(9):
            #attribution de la couleur de la case après sa création
            #si case paire, la case est grise
            if (ligne+colonne)%2 == 0:
                grille.create_rectangle(colonne*CASE, ligne*CASE, (colonne+1)*CASE, (ligne+1)*CASE, fill='#7F7F7F')
            #sinon, la case est noire
            else:
                grille.create_rectangle(colonne*CASE, ligne*CASE, (colonne+1)*CASE, (ligne+1)*CASE, fill='#101010')


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
        label_titre = Label(cadre1, text = 'ERREUR CHOIX', bg = '#404040', fg = 'white', padx = 15, pady = 5, borderwidth = 2)
        label_titre.pack()
        
        print('Veuillez refaire votre choix')


"""  FONCTION QUI GERE LA CREATION DES PIONS  """

#fonction création des pions de la grille en fonction de la liste_grille
def creation_pions(liste_grille, grille, CASE):

    numero_ligne=0
    #liste_grille représentant toutes les cases du grille, on parcours donc la liste pour les lignes
    for ligne in liste_grille:

        numero_colonne=0
        
        #on parcours ensuite la liste pour les lignes
        for colonne in ligne:
            #1 correspond à un pion rouge et 2 correspond à un piont bleu
            if colonne == 1:
                #création du pion rouge
                grille.create_oval(X0+CASE*numero_colonne,Y0+(CASE*numero_ligne),X1+CASE*numero_colonne,Y1+(CASE*numero_ligne), fill='#FF5E4D')

            elif colonne == 2:
                #création du pion bleu
                grille.create_oval(X0+CASE*numero_colonne,Y0+(CASE*numero_ligne),X1+CASE*numero_colonne,Y1+(CASE*numero_ligne), fill='#00CCCB')
               
            numero_colonne = numero_colonne+1

        numero_ligne=numero_ligne+1


"""  FONCTIONS QUI GERENT LE PLACEMENT DES PIONS EN FONCTION DE LA PARTIE  """

#fonction début de partie qui appelle la fonction de création des pions
def debut_partie(cadre1, grille, fenetre, creation_pions):

    label_titre = Label(cadre1, text = 'GOBS DEBUT DE PARTIE', bg = '#404040', fg = 'white', padx = 15, pady = 5, borderwidth = 2)
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

    label_titre = Label(cadre1, text = 'GOBS MILIEU DE PARTIE', bg = '#404040', fg = 'white', padx = 15, pady = 5, borderwidth = 2)
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

    label_titre = Label(cadre1, text = 'GOBS FIN DE PARTIE', bg = '#404040', fg = 'white', padx = 15, pady = 5, borderwidth = 2)
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
def est_dans_grille():

    print('TEST DE COORDONNEES DANS LA GRILLE')
    print('Veuillez saisir le numéro de ligne (la grille va de 1 à 9)')
    ligne = int(input())
    assert type(ligne) == int, "ERREUR SAISIE, Veuillez entrer un nombre entier"

    print('Veuillez saisir le numéro de colonne (la grille va de 1 à 9)')
    colonne = int(input())
    assert type(colonne) == int, "ERREUR SAISIE, Veuillez entrer un nombre entier"

    assert 0 < ligne <= 9 and 0 < colonne <= 9, "ERREUR COORDONNEES, Les coordonnées saisies ne sont pas dans la grille"
    

    print("la case saisie est bien dans la grille")


"""  MAIN  """

#création de la fenetre
fenetre = Tk()
fenetre.title('GOBS Python')
fenetre['bg']='#101010'
fenetre.resizable(False, False)

#lancement de l'interface de jeu
interface(fenetre, creation_grille, joueur)

est_dans_grille()

fenetre.mainloop()