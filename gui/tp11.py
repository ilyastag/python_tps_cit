import tkinter as tk
from tkinter import messagebox

def calculer_somme():
    try:
        # Récupérer les valeurs saisies à partir des StringVar
        valeur1 = float(valeur1_var.get())
        valeur2 = float(valeur2_var.get())
        
        # Calculer la somme
        somme = valeur1 + valeur2
        
        # Afficher la somme dans le label
        resultat_label.config(text=f"Résultat: {somme}")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez saisir des nombres valides.")

def effacer_contenu():
    # Réinitialiser les champs à "0" en utilisant les StringVar
    valeur1_var.set("0")
    valeur2_var.set("0")
    # Réinitialiser le label de résultat
    resultat_label.config(text="Résultat: ")

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calculateur de somme")

fenetre.geometry("300x600")

# Créer des variables Tkinter pour les champs d'entrée
valeur1_var = tk.StringVar(value="0")  # Initialisation avec "0"
valeur2_var = tk.StringVar(value="0")  # Initialisation avec "0"

entry1 = tk.Entry(fenetre, textvariable=valeur1_var, width=220)  
entry1.pack()

entry2 = tk.Entry(fenetre, textvariable=valeur2_var) 
entry2.pack()

# Ajouter le bouton pour calculer la somme
bouton_calculer = tk.Button(fenetre, text="Calculer", command=calculer_somme)
bouton_calculer.pack()

# Ajouter le bouton pour effacer les contenus
bouton_effacer = tk.Button(fenetre, text="Effacer", command=effacer_contenu)
bouton_effacer.pack()

# Ajouter le label pour afficher le résultat
resultat_label = tk.Label(fenetre, text="Résultat: ", font=("Arial", 14))
resultat_label.pack()

# Lancer la boucle principale de Tkinter
fenetre.mainloop()
