from produit import Produit as P
from client import Client as C

import functools


p1=P("PC HP",500.3)
p2=P("Clé USB 64Go",120)
p3=P("Souris Dell",70)
p4=P("Clavier XPro",46.5)
p5=P("Router CISCO 24 ports",700)

c1=C("Zahir Omar","D981000",0.3)

produits=[p1,p2,p3,p4,p5]

    
listprixttc= list(map(lambda x: x.calculerTTC(),produits))
montanttotal=functools.reduce(lambda x,y:x+y,listprixttc)
print(listprixttc)
print(f"{montanttotal:.2f}")

for i,j in zip([1,3,7,9,9],["A","H","K","O","J"]):
    print(i)
    print(j)
