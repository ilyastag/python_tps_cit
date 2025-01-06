class Student:
    def __init__(self, nom, prenom, adresse, date_de_naissance, email,pwd):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.date_de_naissance = date_de_naissance
        self.email = email
        self.pwd = pwd

    def __str__(self):
        return f"Student(nom={self.nom}, prenom={self.prenom}, adresse={self.adresse}, date_de_naissance={self.date_de_naissance}, email={self.email})"