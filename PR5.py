
class Win_Door:
     def __init__(self, x, y):
          self.square = x * y
class Room:
    def __init__(self, x, y, z):
        self.square = 2 * z * (x + y)
        self.wd = []
    def addWD(self, w, h):
        self.wd.append(Win_Door(w, h))
    def workSurface(self):
        new_square = self.square
        for i in self.wd:
            new_square -= i.square
        return new_square

r1 = Room(6, 3, 2.7) 
print(r1.square) #общая  площадь квартиры
r1.addWD(1, 1)  #площадь окна
r1.addWD(1, 1) #площадь окна
r1.addWD(1, 2) #площадь двери
print(r1.workSurface()) 