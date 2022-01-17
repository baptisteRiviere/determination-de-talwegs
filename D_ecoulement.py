"""
Ce module a pour but de construire la matrice d'écoulement à partir du MNT en s'appuyant sur la fonction 'voisin' codée dans la partie C
On va modéliser la pluie, chaque 'case' de la matrice reçoit une goutte, celle-ci va descendre (resp monter) vers le voisin le plus bas (resp le plus haut) 
On sauvegarde l'avancée de la goutte en ajoutant +1 dans la matrice d'écoulement pour chaque nouvelle position, jusqu'à ce que la goutte arrive à un point stable (frontière de l'image ou dans une cuvette)
"""

# les imports
from C_voisinage import dictionnaire_voisins
import numpy as np


# Création de la matrice d'écoulement
def creation_matrice_ecoulement(MNT):
    """
    Renvoie une matrice numpy de zéros de la taille du MNT

    :param MNT: Dictionnaire contenant les informations sur le MNT extraites du fichier asc
    :type MNT: dict
    :return: grille numpy remplie de 0 et de même dimension que MNT['data']
    :returntype: np.array
    """
    Dx = MNT['ncols']
    Dy = MNT['nrows']
    m_ecoulement = np.zeros([Dy,Dx])
    return m_ecoulement


# Fabrication de la matrice
def matrice_ecoulement(MNT,talweg = True):
    """
    Renvoie la matrice d'écoulement à partir du MNT telle qu'elle est décrite dans l'énoncé du module D_ecoulement

    :param MNT: Dictionnaire contenant les informations sur le MNT extraites du fichier asc
    :type MNT: dict
    :talweg: booléen vrai si on s'intéresse aux talwegs, faux si on s'intéresse aux crêtes
    :type talweg: bool
    :return: Matrice d'écoulement 
    :returntype: np.array
    """

    Me = creation_matrice_ecoulement(MNT)
    VOISIN = dictionnaire_voisins(MNT,talweg)

    # on va parcourir la matrice à l'exception des bords (en effet on n'a pas toutes les données pour analyser le voisinage aux frontières)

    for y in range(1,MNT['nrows']-1):
        for x in range(1,MNT['ncols']-1):

            # on modélise l'écoulement de la goutte d'eau, on cherche son voisin le plus haut ou bas
            # puis on laisse la goutte s'écouler en eregistrant ses dernières position dans la liste Trajectoire (sa fonction est décrite ci-dessous)
            [Vx,Vy] = VOISIN[(x,y)]
            Trajectoire = [[Vx,Vy]]

            # On continue l'écoulement tant que la case suivante n'a pas déjà été parcourue par la goutte, qu'elle n'est pas sur une frontière ou qu'elle a un voisin plus bas/haut on continue son parcours 
            while VOISIN[(Vx,Vy)] not in Trajectoire:
                
                # On calcule le nouveau voisin et on enregistre sa position dans Trajectoire
                [Vx,Vy] = VOISIN[(Vx,Vy)]
                Trajectoire.append([Vx,Vy])

                # on peut alors incrémenter la matrice Me
                Me[Vy][Vx] += 1

                # On veut savoir si la goutte stagne entre quelques cases de même altitude (et ainsi éviter de rester dans une boucle infinie), on s'intéresse donc seulement aux dernières valeur de Trajectoire, qui est une liste "garage"
                # C'est pour cela qu'on supprime régulièrement sa première valeur, si la goutte parcourt une longue distance, Trajectoire va être trop longue à parcourir et la complexité temporelle sera trop importante
                # Dans certains cas très particuliers l'algorithme peut tourner en boucle à l'infini: si on a un plateau avec trop de cases de même altitude par exemple, la goutte peut tourner en rond, si cela arrive on peut modifier ou supprimer les lignes suivantes (en mettant plus de 10)
                if len(Trajectoire) > 10:
                    del(Trajectoire[0])

    return Me