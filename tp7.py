import json

with open("eleve.json","r") as file:
    data= json.load(file)
    #print(data)
    h=filter(lambda x: x['isMale']==True,data)
    print(list(h))