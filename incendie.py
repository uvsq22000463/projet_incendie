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

import tkinter as tk

#constante
couleur_fond= "white"
LARGEUR = 600
HAUTEUR = 400

#fonction




#programme principale
racine = tk.Tk()
racine.title("incendie")

#creation de widget
canvas = tk.Canvas(racine, bg = couleur_fond, width = LARGEUR, height = HAUTEUR)

#placement de widget
canvas.grid()

#boucle principale
racine.mainloop
cc
abc
canvas = tk.Canvas(racine, width = 500, height = 500, bg="white") 
LARGEUR = 200
HAUTEUR = 200

canvas.create_line((100,0), (100,500))
canvas.create_line((200,0), (200,500))
canvas.create_line((300,0), (300,500))
canvas.create_line((400,0), (400,500))
canvas.create_line((500,0), (500,500))

canvas.create_line((100,0), (100,500))
canvas.create_line((200,0), (200,500))
canvas.create_line((300,0), (300,500))
canvas.create_line((400,0), (400,500))
canvas.create_line((500,0), (500,500))

canvas.grid(column = 0 , row = 0)

# fonctionnalités liées au choix du terrain:
boutton1 = tk.Button(racine, text =" generer un terrain au hasard" )
boutton1.grid(column = 0, row = 1)

boutton2 = tk.Button(racine, text ="sauvgarder_letat_dun_terrain")
boutton2.grid(column = 0, row = 2)

boutton3 = tk.Button(racine, text ="charger un terrain depuis un fichier")
boutton3.grid(column =0, row = 3)


# fonctionnalités liées à la simulation:

boutton4 = tk.Button(racine, text ="effectuer une étape de simulation")
boutton4.grid(column = 0, row = 4)


boutton5 = tk.Button(racine, text = "démarrer une simulation")
boutton5.grid(column = 0, row = 5)


boutton6 = tk.Button(racine, text = "arrêter la simulation")
boutton6.grid(column = 0, row = 6)


# les fonctions utulisées:
# 1: liée au boutton 1, elle permet de generer un terrain au hasard dans le canvas(random)
# 2: liée au boutton2 permet de sauvgarder_letat_dun_terrain
# 3: liée au boutton3 permet charger un terrain depuis un fichier
# 4: liée au boutton4 permet d'effectuer une étape de simulation"
# 5: liée au boutton5 permet démarrer une simulation"
# 6: liée au boutton6 permet démarrer une simulation arrêter la simulation
