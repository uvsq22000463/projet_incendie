#########################################
# groupe <MIASHS TD02>
# David Daulasim
# Gaetan Bres
# Line-Sephora Assouan
# Sede Saizonou
# Souhaila Chaouch
# Ramata Dia 
# https://github.com/uvsq22000463/projet_incendie
#########################################

# import des librairies
import tkinter as tk
import random as rd
import copy

# définition des constantes (écrites en majuscule)

DUREE_FEU = 10
DUREE_CENDRE = 20
LARGEUR = 600
HAUTEUR = 600
COULEUR_QUADR = 'black'
COTE = 100
NB_COL = LARGEUR // COTE 
NB_LINE = HAUTEUR // COTE
COULEUR = ['blue', 'green', 'yellow']
COULEUR_FOND = rd.choice(COULEUR)


# définition des variables globales:
liste = []



# les fonctions utulisées:


# 2: liée au boutton2 permet de sauvgarder_letat_dun_terrain
# 3: liée au boutton3 permet charger un terrain depuis un fichier
# 4: liée au boutton4 permet d'effectuer une étape de simulation"
# 5: liée au boutton5 permet démarrer une simulation"
# 6: liée au boutton6 permet démarrer une simulation arrêter la simulation


def grille():
    """Affiche un quadrillage sur le canvas."""
    x0, x1 = 0, LARGEUR
    y = 0
    while y <= HAUTEUR:
        canvas.create_line(x0, y, x1, y, fill=COULEUR_QUADR)
        y += COTE
    y0, y1 = 0, LARGEUR
    x = 0
    while x <= LARGEUR:
        canvas.create_line(x, y0, x, y1, fill=COULEUR_QUADR)
        x += COTE

# 1: liée au boutton 1, elle permet de generer un terrain au hasard dans le canvas(random)




def terrain_hasard():
    """permet de générer un terrain au hasard"""
    global c_bleu, c_vert, c_jaune

    global liste
    liste = []
    canvas.delete("all")

    for i in range(1, LARGEUR, COTE):
        for j in range(1, HAUTEUR, COTE):
            liste.append([i, j, rd.choice(COULEUR), 0])
    for n in range(len(liste)):

        if liste[n][2] == "blue":
             c_bleu = canvas.create_rectangle(liste[n][0], liste[n][1], liste[n][0]+COTE, liste[n][1]+COTE, fill="blue")
        elif liste[n][2] == "green":
             c_vert = canvas.create_rectangle(liste[n][0], liste[n][1], liste[n][0]+COTE, liste[n][1]+COTE, fill="green")
        elif liste[n][2] == "yellow":
             c_jaune = canvas.create_rectangle(liste[n][0], liste[n][1], liste[n][0]+COTE, liste[n][1]+COTE, fill="yellow")




def clic_feu(event):
    """Fonction permettant de créer une cellule de feu à l'endroit ou la souris se situe avec un clic gauche"""

    x = event.x
    y = event.y

    for n in range(len(liste)):
        if (liste[n][0] + COTE - 1 >= x >= liste[n][0] and liste[n][1] + COTE - 1 >= y >= liste[n][1] and liste[n][2] != "blue"):
            canvas.create_rectangle(liste[n][0], liste[n][1], liste[n][0]+COTE, liste[n][1]+COTE, fill="red")
            liste[n][2] = "red"
            liste[n][3] = DUREE_FEU


def etape_ij():
    """Fait une étape du jeu de la vie pour la case de coordonnées (i, j):
    retourne la nouvelle valeur à mettre dans le tableau
    """
    return 0


def etape():
    """Fait une étape de simulation"""
    global liste
    # copie du tableau
    nouvelle_liste = copy.deepcopy(liste)
    # traiter toutes les cases du tableau
    for i in range(NB_LINE):
        for j in range(NB_COL):
            nouvelle_liste[i][j] = etape_ij()
    # on modifie le tableau global
    liste = nouvelle_liste


    





# programme principal:
 
racine = tk.Tk()
canvas = tk.Canvas(racine, width = 500, height = 500, bg="white") 


grille()

canvas.grid(column = 0 , row = 0)



# fonctionnalités liées au choix du terrain:
boutton1 = tk.Button(racine, text =" generer un terrain au hasard", command =terrain_hasard )
boutton1.grid(column = 0, row = 1)

boutton2 = tk.Button(racine, text ="sauvgarder_letat_dun_terrain")
boutton2.grid(column = 0, row = 2)

boutton3 = tk.Button(racine, text ="charger un terrain depuis un fichier")
boutton3.grid(column =0, row = 3)


# fonctionnalités liées à la simulation:

boutton4 = tk.Button(racine, text ="effectuer une étape de simulation", command=etape)
boutton4.grid(column = 0, row = 4)


boutton5 = tk.Button(racine, text = "démarrer une simulation")
boutton5.grid(column = 0, row = 5)


boutton6 = tk.Button(racine, text = "arrêter la simulation")
boutton6.grid(column = 0, row = 6)


racine.bind("<KeyPress-a>", etape)
racine.bind("<Button-1>", clic_feu )



racine.mainloop()

