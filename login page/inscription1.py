from customtkinter import (
    CTk,
    CTkButton,
    set_appearance_mode,
    CTkImage,
    CTkLabel,
    CTkComboBox,
    CTkCheckBox,
    CTkSwitch,
    CTkEntry,
    CTkFrame,
)
from PIL import Image

# Initialiser l'application
app = CTk()

# Définir la taille de la fenêtre
app.geometry("600x600")

# Configurer le mode d'apparence
set_appearance_mode("dark")

# Créer un cadre centré
f = CTkFrame(master=app, border_color='yellow', border_width=2, width=330, height=550)
f.place(relx=0.5, rely=0.5, anchor='center')

# Charger l'image
image_path = r"C:\Users\thinkpad\Desktop\ux\112.png"
try:
    img = Image.open(image_path)
    ctk_img = CTkImage(light_image=img, size=(50, 50))  # Taille personnalisée
except FileNotFoundError:
    print(f"Le fichier {image_path} est introuvable.")
    ctk_img = None

# Créer un label centré
label = CTkLabel(master=f, text="Welcome to CIT", font=("Math Sans bold Italic", 20))
label.place(relx=0.5, rely=0.1, anchor="center")

# Créer une sélection d'options
combobox = CTkComboBox(
    master=f,
    values=["Instructeur", "Stagiaire Info1"],
    dropdown_fg_color="black",
    border_color="yellow",
    fg_color="purple",
    font=("Helvetica", 12),
)
combobox.place(relx=0.5, rely=0.2, anchor="center")

# Créer un bouton centré avec une image d'inscription
if ctk_img:
    button = CTkButton(
        master=f,
        text="INSCRIPTION",
        corner_radius=18,
        fg_color="purple",
        image=ctk_img,
        hover_color="yellow",
        border_color="yellow",
        border_width=2,
    )
    button.place(relx=0.5, rely=0.78, anchor="center")

# Créer une entrée de texte
entry_name = CTkEntry(
    master=f,
    placeholder_text="Nom",
    corner_radius=18,
    border_color="purple",
    border_width=2,
)
entry_name.place(relx=0.5, rely=0.29, anchor="center")

# Créer une entrée de mot de passe
entry_password = CTkEntry(
    master=f,
    placeholder_text="Mot de passe",
    show="*",
    corner_radius=18,
    border_color="purple",
    border_width=2,
)
entry_password.place(relx=0.5, rely=0.35, anchor="center")

# Créer des cases à cocher
checkbox_login = CTkCheckBox(
    master=f,
    text="S'identifier",
    fg_color="purple",
    corner_radius=18,
    border_color="purple",
    border_width=2,
)
checkbox_login.place(relx=0.37, rely=0.62, anchor="center")

checkbox_register = CTkCheckBox(
    master=f,
    text="S'inscrire",
    fg_color="purple",
    corner_radius=18,
    border_color="yellow",
    border_width=2,
)
checkbox_register.place(relx=0.69, rely=0.62, anchor="center")

# Créer un switch
switch_validate = CTkSwitch(
    master=f,
    text="J'accepte les conditions",
    fg_color="purple",
    border_color="yellow",
    button_hover_color="yellow",
    progress_color="purple",
    border_width=2,
)
switch_validate.place(relx=0.53, rely=0.9, anchor="center")

# Ajouter un bouton supplémentaire
if ctk_img:
    output_button = CTkButton(
        master=f,
        text="Connexion",
        corner_radius=18,
        fg_color="purple",
        image=ctk_img,
        hover_color="yellow",
        border_color="yellow",
        border_width=2,
    )
    output_button.place(relx=0.5, rely=0.47, anchor="center")

# Lancer l'application
app.mainloop()
