#demander 7 notes des élèves
#calculer la moyenne
#affichier toutes les notes
#afficher la moyenne avec 2 chiffres après la virgule.

notes=[]
s=0
ic=0
#for i in range(7):
n=float(input(f"saisir la note {ic+1}:"))
while n>=0:
    notes.append(n)
    s=s+n
    n=float(input(f"saisir la note {ic+1}:"))
    ic=ic+1

moyenne=s/len(notes)
print(f"Ta moyenne = {moyenne:.2f}/20")

counter=0
for k in notes:
    if k>=moyenne:
        counter=counter+1

print(f"nombre de notes >= moyenne : {counter}")
rapport= counter/len(notes)
print(f"Pourcentage = {rapport:.2%}")


print(notes)
notes.reverse()
print(notes)
print(notes.count(6))
