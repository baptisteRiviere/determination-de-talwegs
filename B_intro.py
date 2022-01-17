""" 
Module contenant les fonctions permettant d'afficher et de rogner le MNT
"""


def affiche(MNT):
    """
    Affiche le MNT

    Il est cependant nécessaire d'écrire un show() ou plt.show() hors de la fonction !!

    :MNT: Dictionnaire contenant les informations sur le MNT extraites du fichier asc
    """
    from matplotlib.pyplot import matshow
    matshow(MNT['data'])


def SousPartieMNT(MNT,X,Y,Dx,Dy):
    """
    Partitionne le MNT :
    Retourne une partie du MNT, le rectangle dont le coin supérieur gauche est le couple (ligne,colonne) = (X,Y)
    et dont le nombre de ligne (resp de colonnes) est Dx (resp Dy)
    Attention : on ne donne pas en argument les coordonnées en mètre

    :MNT: Dictionnaire contenant le MNT (les clés sont rapelées dans openAsc)
    :param X: entier représentant la coordonnée en x du coin sup gauche du nouveau MNT
    :type X: int
    :param Y: entier représentant la coordonnée en y du coin sup gauche du nouveau MNT
    :type Y: int
    :param Dx: (resp :param Dy:) nombre de lignes (resp colonnes) du nouveau MNT 
    :type Dx: (resp :type Dy:) int
    :return: Dictionnaire du même type de l'entrée "MNT" avec la grille rognée
    :returntype: dict
    """
    from numpy import zeros

    # On cherche les nouveaux xllcorner et yllcorner
    dx,dy = MNT['dx'],MNT['dy']
    X1 = MNT['xllcorner'] + X*dx
    Y1 = MNT['yllcorner'] - Y*dy

    # Création du dictionnaire
    NewMNT = {}
    NewMNT['ncols'] = Dx
    NewMNT['nrows'] = Dy
    NewMNT['xllcorner'] = X1
    NewMNT['yllcorner'] = Y1
    NewMNT['dx'] = dx
    NewMNT['dy'] = dy
    NewMNT['data'] = zeros((Dy,Dx))

    # il reste à parcourir le MNT d'origine pour copier les valeurs
    for ligne in range(Dy):
        for col in range(Dx):
            NewMNT['data'][ligne][col] = MNT['data'][Y+ligne][X+col]
    
    return NewMNT