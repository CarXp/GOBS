
#
#            _______ ______  _____ _______ _____ 
#           |__   __|  ____|/ ____|__   __/ ____|
#              | |  | |__  | (___    | | | (___  
#              | |  |  __|  \___ \   | |  \___ \ 
#              | |  | |____ ____) |  | |  ____) |
#              |_|  |______|_____/   |_| |_____/ 
#                                      
#                                      
# ==================================================================

grille  =  [[1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2]]


def test_condition_fin(grille):

    condition_fin = False
    pions_x, pions_o = 0,0

    #on parcours la grille pour voir le nombre de pions
    for pions in grille[0]:
        if pions == 2:
            pions_x += 1

        elif pions == 1:
            pions_o += 1

    if pions_x < 6 or pions_o < 6:
        condition_fin = True

    #si la condition de fin est fausse, on continue
    if condition_fin:
        assert pions_x >= 6 or pions_o >= 6, "erreur condition fin de jeu"
        print('Le jeu est en cours de partie')
    
    #sinon le jeu est fini
    else:
        assert pions_x < 6 or pions_o < 6, "erreur condition fin de jeu"
        print("Le jeu est fini")

    return condition_fin


def test_grille_lancement(grille):

    assert grille == [[1, 1, 1, 1, 1, 1, 1, 1, 1],\
                      [1, 1, 1, 1, 1, 1, 1, 1, 1],\
                      [1, 1, 1, 1, 1, 1, 1, 1, 1],\
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],\
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],\
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],\
                      [2, 2, 2, 2, 2, 2, 2, 2, 2],\
                      [2, 2, 2, 2, 2, 2, 2, 2, 2],\
                      [2, 2, 2, 2, 2, 2, 2, 2, 2]]\
, "Erreur d'initialisation de la grille"
    print("L'affichage de la grille au lancement du programme est valide")

def test_tour():

    print('debut des tests pour le tour de jeu')
    tour = 0

    while tour <= 2:

        if tour % 2 == 0:
            assert tour % 2 == 0, "erreur condition"
            print('tour du joueur X')
        
        else:
            assert tour % 2 != 0, "erreur condition"
            print('tour du joueur O')

        tour += 1

#fonction lancement de tests
def run_test(grille):

    print('Debut des tests\n')

    #lancement test "test_condition_fin"
    test_condition_fin(grille)
    print('Fin des tests de condition de fin\n')

    #lancement test "test_grille_lancement"
    test_grille_lancement(grille)
    print('Fin des tests de la grille de lancement\n')

    #lancement test "test_tour"
    test_tour()
    print('Fin de test de tour de jeu\n')

    print('Fin des tests')

run_test(grille)