# -*- coding: utf-8 -*-

    # Import ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from math import *
from fonctions import *
from Fleur import *
from threading import *
from Tkinter import *

import time
parametres = charger_parametres()

argent = 5

fleurs = list()
for i in range(12):
    fleurs.append(None)


def arroser_fleur():

    try:
        fleur = fleurs[int(choix_fleur.get())]
    except ValueError:
        return None

    if fleur is not(None):
        fleur.eau(100)


def acheter_fleur():
    
    global argent
    
    try:
        fleur = fleurs[int(choix_fleur.get())]
    except ValueError:
        return None
        
    if fleur is None and argent >= 5: 
        for i in range(len(boutons_fleur)):
            if choix_fleur.get() == str(i):
                boutons_fleur[i].config(image=photo_fleur)
                fleurs[i] = Fleur()
                argent -= 5
                print(argent)                
                
def jeter_fleur():
    for i in range(len(boutons_fleur)):
        if choix_fleur.get() == str(i):
            boutons_fleur[i].config(image=photo_pot)
            fleurs[i] = None


def vendre_fleur():
    
    global argent    
    
    try:
        fleur = fleurs[int(choix_fleur.get())]
    except ValueError:
        return None
        
    if fleur is not(None):
        if fleur.croissance == 1000:
            argent += round(fleur.vitalite, -2)/100
            jeter_fleur()
            print(argent)

def main():

    continuer = True

    while continuer:

        for fleur in fleurs:
            if fleur is not(None):
                fleur.tic()

        if choix_fleur.get() == "":
            label_stats.configure(label_stats, text="\nCroissance : {}\n\nHydratation : {}\n\nVitalité : {}".format(0, 0, 0))

        elif fleurs[int(choix_fleur.get())] is None:
            label_stats.configure(label_stats, text="\nCroissance : {}\n\nHydratation : {}\n\nVitalité : {}".format(0, 0, 0))

        else:
                choix = int(choix_fleur.get())
                label_stats.configure(label_stats, text="\nCroissance : {}\n\nHydratation : {}\n\nVitalité : {}".format(fleurs[choix].croissance, fleurs[choix].hydratation, fleurs[choix].vitalite))
        time.sleep(eval(parametres["VitesseTic"]))

programme = Thread(target=main)

    # Fenêtre ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fenetre = Tk()

fenetre.title("Flower Simulator")

fenetre.resizable(width=False, height=False)

    # Alerte temporaire ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def alert():
    tkinter.messagebox.showinfo("CE BOUTON NE MARCHE PAS ENCORE !", "Vous venez de cliquer sur un bouton qui n'a pas encore été assigné.")

    # Menubar ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichier", menu=menu1)
menu1.add_command(label="Charger", command=alert)
menu1.add_command(label="Sauvegarder", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)

menu2 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Shop", menu=menu2)
menu2.add_command(label="Eau", command=alert)
menu2.add_command(label="Engrais", command=alert)
menu2.add_command(label="Plantes", command=alert)

menu3 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Aide", menu=menu3)
menu3.add_command(label="Accès fichier Python", command=alert)
menu3.add_command(label="A propos", command=alert)

fenetre.config(menu=menubar)

    # Canvas & Image ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

canvas = Canvas(fenetre, width=700, height=500, bg="white")
canvas.pack(side=LEFT, padx=5, pady=5)

photo_fleur = PhotoImage(file="fleur.png")
photo_pot = PhotoImage(file="fleur_pot.png")
message = PhotoImage(file="message.png")

choix_fleur = StringVar()
# Création des boutons des fleurs

boutons_fleur = list()
for i in range(12):
    boutons_fleur.append(Radiobutton(canvas, image=photo_pot, bg="white", variable=choix_fleur, value=i))

# Placement des boutons des fleurs
canvas.create_window(10, 20, anchor=NW, window=boutons_fleur[0])
canvas.create_window(10, 185, anchor=NW, window=boutons_fleur[1])
canvas.create_window(10, 350, anchor=NW, window=boutons_fleur[2])
canvas.create_window(175, 20, anchor=NW, window=boutons_fleur[3])
canvas.create_window(175, 185, anchor=NW, window=boutons_fleur[4])
canvas.create_window(175, 350, anchor=NW, window=boutons_fleur[5])
canvas.create_window(350, 20, anchor=NW, window=boutons_fleur[6])
canvas.create_window(350, 185, anchor=NW, window=boutons_fleur[7])
canvas.create_window(350, 350, anchor=NW, window=boutons_fleur[8])
canvas.create_window(520, 20, anchor=NW, window=boutons_fleur[9])
canvas.create_window(520, 185, anchor=NW, window=boutons_fleur[10])
canvas.create_window(520, 350, anchor=NW, window=boutons_fleur[11])

canvas.pack()

    # Labels ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

label_stats = Label(fenetre, width=20, height=5, text="\nCroissance : {}\n\nHydratation : {}\n\nVitalité : {}".format(0, 1000, 1000), relief=FLAT, fg='black', command=None)
label_stats.pack(side=TOP, padx=5, pady=5)
label_stats.config(fg='Black', bd=12)

bouton_arroser = Button(fenetre, width=25, height=5, text="Arroser la fleur", command=arroser_fleur)
bouton_acheter = Button(fenetre, width=25, height=5, text="Acheter une fleur", command=acheter_fleur)
bouton_vendre = Button(fenetre, width=25, height=5, text="Vendre la fleur", command=vendre_fleur)
bouton_jeter = Button(fenetre, width=25, height=5, text="Jeter la fleur", command=jeter_fleur)

bouton_jeter.pack(side=BOTTOM, padx=5, pady=5)
bouton_vendre.pack(side=BOTTOM, padx=5, pady=5)
bouton_acheter.pack(side=BOTTOM, padx=5, pady=5)
bouton_arroser.pack(side=BOTTOM, padx=5, pady=5)

    # Mainloop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

programme.start()
fenetre.mainloop()
