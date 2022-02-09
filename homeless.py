import random
"""actividad en clase del bagabundo"""
class Homeless:
    def __init__(self, name,x=0,y=0):
        self.name = name
        self.x = x
        self.y = y


    def posicion (self):
        return (self.x,self.y)

    def distance(self,other_coordinate):
        return (self.x**2 + self.y**2)**0.5

class StandarHomeless(Homeless):
    def __innit__(self, name):
        super().__init__(name)

    def walk(self):
        dx,dy= random.choice([(1,0),(-1,0),(0,1),(0,-1)])
        self.x +=dx
        self.y +=dy
        return [self.x,self.y]


class ModerateHomeless(Homeless):
    def __init__(self, name):
        super().__init__(name)
    def walk(self):
        dx,dy = random.choice([(0,2),(0,-2),(2,0),(-2,0)])
        self.x +=dx
        self.y +=dy
        return [self.x,self.y]



class leftHomeless(Homeless):
    def __init__(self, name):
        super().__init__(name)
    def walk(self):
        dx,dy = random.choice([(0,1),(0,-1),(1,0),(-5,0)])
        self.x +=dx
        self.y +=dy
        return [self.x,self.y]

"""Super es para heredar de la clase padre"""



"""el random.choice tiene 2 argumentos 1,0. pero puede tener mas de estos como unos 5 o 6 dimensiones o datos"""

"""git branch nombre = crear nueva master.
git branch = visualizar las master.
git checkout master = cambia de master"""