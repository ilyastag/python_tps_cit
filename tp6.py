import json

eleve= {
    "nom":"Ahmadi",
    "prenom":"Omar",
    "age":17,
    "isMale": True,
    "note":15.6
}

elevestring=json.dumps(eleve)
print(elevestring)

with open("eleve.json","w") as file:
    json.dump(eleve,file)

