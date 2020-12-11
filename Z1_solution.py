
import math

class WinDoor:  # площадь окна или двери
    def __init__(self, x, y): # инициализация
        self.square = x * y # считаем площадь окна или двери

class Room: 
    def __init__(self, x, y, z):
        self.square = 2 * z * (x + y) # площадь стен без потолка и пола 
        self.wd = [] # пустой список, список окон и дверей 

    def addWD(self, w, h): # фун-ция / метод, который добравляет в пустой список объекты 
        self.wd.append(WinDoor(w, h)) # append - добавление в список площадь окна или двери
    
    def workSurface(self):
        new_square = self.square # площадь стен / обоев без окон и дверей 
        for i in self.wd:
            new_square -= i.square # вычитание из площади комнаты окон и дверей
        return new_square

class Room2: # класс, для изменения данных комнаты
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.wd = []

    def change_room_znach(self, x, y, z): # метод, меняющий значения
        self.x = x
        self.y = y
        self.z = z

    def square(self):  # подсчет новой площади 
        return 2 * self.z * (self.x + self.y) # площадь стен 

    def addWD(self, w, h): # подсчет дверей и окон 
        self.wd.append(WinDoor(w, h))

    def workSurface(self): # подсчет новой площади без дверей и окон 
        new_square = self.square()
        for i in self.wd:
            new_square -= i.square
        return new_square
        
    def rulon(self, height, width):# кол-во рулонов
        rulon_square = height * width # площадь 1 рулона
        walls = self.workSurface()  # подтягиваем новую площадь без дверей и окон 
        count = math.ceil(walls / rulon_square) # считаем кол-во рулонов, округляем до большего
        return count
    

r1 = Room2(6, 5, 2.7)

print('Площадь комнаты = ', r1.square())
r1.addWD(1, 1) # 1 окно
r1.addWD(1, 1) # 2 окно
r1.addWD(1, 2) # дверь
print('Площадь комнаты без дверей и окон = ', r1.workSurface())
print('Кол-во рулонов = ', r1.rulon(4, 6))

r1.change_room_znach(8, 5, 4)
print('Новая площадь комнаты = ',r1.square())
print('Новая площадь комнаты без дверей и окон = ',r1.workSurface())
print('Кол-во рулонов = ', r1.rulon(4, 6))