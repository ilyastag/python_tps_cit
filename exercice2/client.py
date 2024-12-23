class Client:
    def __init__(self,a,b,c):
        self.__nom=a
        self.__cin=b
        self.__remise=c

    
    def getNom(self):
        return self.__nom
    
    def getCIN(self):
            return self.__cin
    
    def getRemise(self):
            return self.__remise
    
    def setNom(self,m):
        self.__nom=m
    
    def setCIN(self,cin):
            self.__cin=cin
    
    def setRemise(self,r):
            self.__remise=r

    def __repr__(self):
          return f"C[{self.__nom}-{self.__cin}]".upper()
    