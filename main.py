# -*- coding: utf-8 -*-

######################################################################
#    Partiel Python ENSG 2020-2021 Rivière Baptiste, Roineau Lubin   #
######################################################################

#-- Définition des imports --#

import matplotlib.pyplot as plt
from A_open_asc import openAsc
from B_intro import SousPartieMNT
from B_intro import affiche
from C_voisinage import voisin
from D_ecoulement import matrice_ecoulement
from E_resultats import determination_talwegs

#-- Ouverture du MNT --#

MNT = openAsc("mnt_5m.asc")

############################################################
#                         Tests                            #
############################################################

#-- Test de la fonction qui partitionne le MNT --#

print('\nTest Fonction SousPartie\n')
print("\nAttendu:\n2 partitions différentes du MNT de base \nRésultat:")

MNT_test_1 = SousPartieMNT(MNT, 900, 500, 400, 400)
MNT_test_2 = SousPartieMNT(MNT, 900, 200 , 400, 200)

affiche(MNT)
plt.title("MNT complet")
affiche(MNT_test_1)
plt.title("Première partition")
affiche(MNT_test_2)
plt.title("Deuxième Partition")
plt.show()

#-- Test fonction qui analyse les voisins --#

print("___________________________________________________________________________")
print('\nTest Fonction voisin\n')
print("Attendu:\nLes coordonnées du point d'altitude le plus bas voisin du point [29,45] pour MNT_test_1, et celles du points d'altitude le plus haut voisin du point [101,55] pour MNT_test_2\n")
voisin_MNT_Test_1 = voisin(MNT_test_1,29,45,talweg = True)
voisin_MNT_Test_2 = voisin(MNT_test_2,101,55,talweg = False)
print("Résultat:\npoint d'altitude minimale pour le point [29,45] de la sous-partie 1 :", voisin_MNT_Test_1, "\npoint d'altitude maximale pour le point [101,55] de la sous-partie 2 :", voisin_MNT_Test_2)

def Affiche_valeur_des_voisins(MNT,x,y):
    """
    Permet simplement d'afficher les 9 cases autour de x et y pour les tests
    """
    print([x-1,y-1],":",MNT['data'][y-1][x-1],'\t',[x,y-1],":",MNT['data'][y-1][x],'\t',[x+1,y-1],":",MNT['data'][y-1][x+1])
    print([x-1,y],":",MNT['data'][y][x-1],'\t',[x,y],":",MNT['data'][y][x],'\t',[x+1,y],":",MNT['data'][y][x+1])
    print([x-1,y+1],":",MNT['data'][y+1][x-1],'\t',[x,y+1],":",MNT['data'][x+1][y+1],'\t',[x+1,y+1],":",MNT['data'][y+1][x+1])
    
print("\nPoints voisins du premier MNT pour vérification:\n")
print(Affiche_valeur_des_voisins(MNT_test_1,29,45))  
    
print("\nPoints voisins du deuxième MNT pour vérification:\n")
print(Affiche_valeur_des_voisins(MNT_test_2,101,55))  

print("\nCas d'un point frontière:\n")
voisin_MNT_Test_3 =  voisin(MNT_test_1,29,0,talweg = True)
print("point d'altitude minimale pour le point [29,0] de la sous-partie 1 :", voisin_MNT_Test_3)

#-- Test matrice d'écoulement --#

print("___________________________________________________________________________")
print('\nTest Fonction matrice_ecoulement\n')
print("Attendu:\nDeux matrices simulant l'écoulement d'une goutte pour nos 2 sous-parties test\n")
Me1 = matrice_ecoulement(MNT_test_1,talweg = True)
Me2 = matrice_ecoulement(MNT_test_2,talweg = False)
print("Resultat:\n")
plt.matshow(Me1)
plt.matshow(Me2)
plt.show()

#-- Test détermination des talwegs --#

print("___________________________________________________________________________")
print('\nTest Fonction détermination Talwegs\n')
print("Affichage des talwegs pour la 1ère sous-partie, et des lignes de crêtes pour la 2ème sous-partie:\n")
Lx,Ly = determination_talwegs(Me1,0.05)
Lx2,Ly2 = determination_talwegs(Me2,0.05)

print("Resultat:\n")

affiche(MNT_test_1)
plt.scatter(Lx,Ly,color = 'white',s=0.05,marker='*')
plt.title("Talwegs de MNT_test_1")
affiche(MNT_test_2)
plt.scatter(Lx2,Ly2,color = 'red', s=0.05, marker = '*')
plt.title("Lignes de crêtes de MNT_test_2")
plt.show()

print("___________________________________________________________________________")



##########################################################################
#                       Opération sur le MNT complet                     #
##########################################################################


test_complet = False


if test_complet == True:
    print('\nDétermination des talwegs et lignes de crêtes du MNT entier:\n')
    print('\nPatience, ça prend du temps ...\n')
    
    Me_t = matrice_ecoulement(MNT,talweg = True)
    Me_lc = matrice_ecoulement(MNT,talweg = False)
    
    Lx3,Ly3 = determination_talwegs(Me_t,0.01)
    Lx4,Ly4 = determination_talwegs(Me_lc,0.01)
    
    affiche(MNT)
    plt.scatter(Lx3,Ly3,color = 'white', s=0.01, marker = '*')
    plt.title("Talwegs")
    plt.savefig('talweg.png')
    affiche(MNT)
    plt.scatter(Lx4,Ly4,color = 'red', s=0.01, marker = '*')
    plt.title("Lignes de crêtes")
    plt.savefig('ligne_de_cretes.png')
    plt.show()


