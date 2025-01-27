
with open("fichier.txt", "r") as fichier:
    contenu = fichier.read()
    print(contenu)
# Le fichier est automatiquement fermé ici, 
# même en cas d'erreur.


#Equivalent sans with :
fichier = open("fichier.txt", "r")
try:
    contenu = fichier.read()
    print(contenu)
finally:
    fichier.close()


