"""
Ce module contient la fonctions permettant de calculer les talwegs ou les crêtes et de les afficher grâce aux fonctions précédentes
"""

# Les imports
import numpy as np


def determination_talwegs(Me,seuil_rel,talweg = True):
    """
    Renvoie les coordonnées des talwegs du MNT (si talweg = True) ou des crêtes (si talweg = False)calculées à partir de la matrice d'écoulement et d'un seuil

    Calcul du seuil absolu : l'utilisateur pourrait rentrer lui même un seuil absolu mais l'algorithme serait moins autonome
    Par exemple si seuil_rel = 0.01 on va retenir toutes les valeurs supérieures à 0.01*val_max 

    Remarque : on ne fait pas attention aux frontières du MNT : si une goutte arrive à la frontuère elle va s'arrêter et non s'écouler sur le bord du MNT, on ne contabilise pas plus de gouttes aux frontières

    :param Me: Matrice d'écoulement (grille np.array) de même dimension que le MNT
    :type Me: np.array
    :param seuil_rel: seuil relatif à partir duquel on considère qu'on a un talweg ou une crête, il s'agit donc d'un flottant compris entre 0 et 1
    :type seuil_rel: float
    :param talweg: booléen vrai si on s'intéresse aux talwegs, faux si on s'intéresse aux crêtes
    :type talweg: bool
    :return: Lx et Ly listes contenant respectivement les coordonnées suivant x et y, des talwegs ou des crêtes 
    :returntype: list
    """ 
    # on récupère les dimensions de la matrice d'écoulement 
    (nb_lignes, nb_col) = np.shape(Me)

    # on va mettre chaque couple de coordonnées respectant la condition dans les listes (une matrice presque vide serait trop lourde)
    Lx,Ly = [],[]

    # Calcul du seuil absolu
    seuil_abs = seuil_rel * np.max(Me) 
    
    # on n'a plus qu'à parcourir à nouveau la grille et rentrer les coordonnées retenues dans Lx et Ly
    for ligne in range(nb_lignes):
        for col in range(nb_col):
            if Me[ligne][col] > seuil_abs:
                Lx.append(col)
                Ly.append(ligne)

    return Lx,Ly



