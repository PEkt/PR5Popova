from windoor import *
r1 = room.Room(6, 3, 2.7) 
print(r1.square) #общая  площадь квартиры
r1.addWD(1, 1)  #площадь окна
r1.addWD(1, 1) #площадь окна
r1.addWD(1, 2) #площадь двери
print(r1.workSurface()) 


