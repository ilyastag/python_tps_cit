class Produit:
    tva=0.2

    def __init__(self,a,b):
        self.__marque=a
        self.__prix=b
        self.__tva=Produit.tva

    def getMarque(self):
        return self.__marque
    
    def getPrix(self):
            return self.__prix
    
    def getTVA(self):
            return self.__tva
    
    def setMarque(self,m):
        self.__marque=m
    
    def setPrix(self,p):
            self.__prix=p
    
    def setTVA(self,tva):
            self.__tva=tva

    def calculerTTC(self):
          return self.__prix*(1+self.__tva)

    def __repr__(self):
          return f"P[{self.__marque}]".upper()
    