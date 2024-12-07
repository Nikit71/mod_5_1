#   Домашняя работа по уроку "Атрибуты и методы объекта"
#   Задача "Developer - не только разработчик":
from os import close

class House:
    def __init__(self, name, number_of_floors):
        self.name = (name)  #   имя
        self.number_of_floors =number_of_floors   #     кол - во этажей
    def go_to(self,new_floor):
        floor=int(new_floor)
        if floor <= self.number_of_floors:
            for i in range(floor):
                print(i+1)
        else:
            print('"Такого этажа не существует"')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)


