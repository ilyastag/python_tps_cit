class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"Point({self.x:.2f},{self.y:.2f})"
    
    def __add__(self,other):
        if other is None:
            raise TypeError("le 2eme operant ne doit pas etre null ")
        
        if isinstance(other,Point):
            return Point(self.x+other.x,self.y+other.y)
        
        if isinstance(other,(int,float)):
            return Point(self.x+other,self.y+other)
        else:
            raise TypeError("2eme operant non compatible")
        
    
    def __mul__(self,other):
        return Point(self.x*other,self.y*other)
        


        

    