import tkinter as tk
from tkinter import PhotoImage

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Interface avec Grid()")

# Définir les couleurs
couleur_fond = "lightblue"
couleur_haut = "limegreen"
couleur_bas = "orange"
couleurs_lables = ["red", "yellow", "green"]

# Configurer la fenêtre
fenetre.config(bg=couleur_fond)
fenetre.geometry("400x600")

phimag=PhotoImage(file="D:\python_tps_cit\gui\clipartcalc.png")

label1 = tk.Label(fenetre, text="",image=phimag, bg=couleur_haut)
label1.grid(row=0, column=0, columnspan=3,sticky="nsew",padx=5,pady=5)

label2 = tk.Label(fenetre, text="", bg=couleurs_lables[0])
label2.grid(row=1, column=0,sticky="nsew",padx=5,pady=0)

label3 = tk.Label(fenetre, text="", bg=couleurs_lables[1])
label3.grid(row=1, column=1,sticky="nsew",padx=0,pady=0)

label4 = tk.Label(fenetre, text="", bg=couleurs_lables[2])
label4.grid(row=1, column=2,sticky="nsew",padx=5,pady=0)

label5 = tk.Label(fenetre, text="", bg=couleur_bas)
label5.grid(row=2, column=0, columnspan=3,sticky="nsew",padx=5,pady=5)


fenetre.grid_columnconfigure(0, weight=1)
fenetre.grid_columnconfigure(1, weight=1)
fenetre.grid_columnconfigure(2, weight=1)

fenetre.grid_rowconfigure(0, weight=3)
fenetre.grid_rowconfigure(1, weight=1)
fenetre.grid_rowconfigure(2, weight=3)

# Lancer la boucle principale
fenetre.mainloop()