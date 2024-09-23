class House:
    houses_history = []                                           #module_5_4.py

    def __new__(cls, *args):                                      #module_5_4.py
        cls.houses_history.append(args[0])
        return object.__new__(cls)
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):                                            #module_5_4.py
        print(f"{self.name} снесён, но он останется в истории")

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if i >= 1 and i <= self.number_of_floors:
                print(i)
            else:
                print(f'"Этажа {i} в  {self.name}  не существует"')
                break

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, количество этажей: {self.number_of_floors}')

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return isinstance(other, House) and self.number_of_floors == other
        else:
            print('None')

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        elif isinstance(value, House):
            return House(self.name, self.number_of_floors + value.number_of_floors)
        else:
            print('None')

    def __iadd__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        else:
            print('None')

    def __radd__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        else:
            print('None')

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            print('None')

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print('None')

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            print('None')

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print('None')

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors  
        else:
            print('None')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)