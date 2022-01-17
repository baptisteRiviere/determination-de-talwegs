"""
Ce module contient les fonctions permettant d'analyser le voisinage de chaque point et de créer un dictionnaire contenant les coordonnées du point voisin le plus haut ou le plus bas pour chaque coordonnée
"""

def voisin(MNT,x,y,talweg = True):
    """
    Permet d'analyser les 8 voisins d'une case de la matrice,et de déterminer le voisin avec l'altitude la plus basse (talweg) ou la plus haute (ligne de crête) selon que l'argument talweg est vrai ou non

    Remarque : si un voisin est à la même hauteur que la case étudiée on permet à la goutte de s'y écouler

    S'il n'y a pas de voisins strictement plus bas (ou plus haut si talweg = False) ou si on est sur une frontière du MNT : on renvoie le même couple [x,y]

    :param MNT: Dictionnaire contenant les informations sur le MNT extraites du fichier asc
    :type MNT: dict
    :x: coordonnée suivant x du point dont on veut analyser le voisinage
    :y: coordonnée suivant y du point dont on veut analyser le voisinage
    :type x: int
    :type y: int
    :param talweg: booléen vrai si on s'intéresse aux talwegs (renvoie le voisin le plus bas), faux si on s'intéresse aux crêtes (renvoie le voisin le plus haut)
    :type talweg: bool
    :return: coordonnées du point voisin le plus haut ou le plus bas sous la forme d'une liste [x,y]
    :returntype: list
    """

    # on traite le cas où on est sur un bord du MNT
    if (x == 0) or (x == MNT['ncols']-1) or (y == 0) or (y == MNT['nrows']-1): 
        return [x,y]

    # on va chercher la valeur minimale ou maximale des voisins, on initialise avec le point central [x,y]
    voisin,alt_extreme = [x,y],MNT['data'][y][x]

    # on parcourt les 8 cases voisines
    for (ligne,col) in [(y+1,x+1),(y+1,x),(y+1,x-1),(y,x+1),(y,x-1),(y-1,x+1),(y-1,x),(y-1,x-1)]:
            alt_etud = MNT['data'][ligne][col]

            if talweg and alt_etud <= alt_extreme:  
            # on s'intéresse dans ce cas aux talwegs et on a un voisin plus bas
                voisin,alt_extreme = [col,ligne],alt_etud

            elif not talweg and alt_etud >= alt_extreme : 
            # dans ce cas on étudie les crêtes et on a un voisin plus haut
                voisin,alt_extreme = [col,ligne],alt_etud
                
    return voisin



def dictionnaire_voisins(MNT,talweg=True):
    """
    Crée un dictionnaire contenant le voisin le plus bas (ou le plus haut selon la valeur de talweg) pour chaque corrdonnée du MNT

    Remarque : la création d'un dictionnaire permet d'améliorer la complexité temporelle de l'algorithme, en effet on aurait pu utiliser la fonction "voisin" directement dans le module D_ecoulement mais on aurait multiplié les comparaisons par 8 à chaque nouvelle recherche de voisin

    :param MNT: Dictionnaire contenant les informations sur le MNT extraites du fichier asc
    :type MNT: dict
    :param talweg: booléen vrai si on s'intéresse aux talwegs (renvoie le voisin le plus bas), faux si on s'intéresse aux crêtes (renvoie le voisin le plus haut)
    :type talweg: bool
    :return: dictionaire de la forme {(x,y) : [Vx,Vy])}
    :returntype: dict
    """
    dico = {}
    for y in range(MNT['nrows']):
        for x in range(MNT['ncols']):
            # on cherche le voisin le plus haut ou bas
            dico[(x,y)] = voisin(MNT,x,y,talweg)
    return dico

