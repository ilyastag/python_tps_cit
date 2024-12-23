import tkinter as tk

# Création de la fenêtre principale
window = tk.Tk()

window.title("Interface Graphique avec Tkinter")
window.geometry("700x300")  # Taille de la fenêtre (largeur x hauteur)
window.configure(background="lightgreen")
#window.state("zoomed")
#window.attributes("-fullscreen",False)



# Ajout d'un widget Label
label = tk.Label(window, text="Bonjour, bienvenue sur Tkinter !", fg="red",bg="cyan", font=("Arial", 16))
label.pack(pady=20)

label2 = tk.Label(window, text="Officiers CIT 2025", fg="Green",bg="yellow",font=("Arial", 24))
label2.pack(pady=0,fill="both",expand=True)



# Boucle principale de l'interface
window.mainloop()
