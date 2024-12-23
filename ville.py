class Ville:
    total_instance=0
    population=50000

    def __init__(self,n,g,c) :
        self.__nom=n
        self.region=g
        self.codepostal=c
        self.population=Ville.population
        Ville.total_instance+=1










    
    def getNom(self):
        return self.__nom
    
    def setNom(self,n):
        self.nom=n
    
    def getRegion(self):
        return self.region
    
    def setRegion(self,g):
        self.region=g
    
    def __repr__(self) -> str:
        return f"|City :{self.__nom} - {self.region}|"
    

    