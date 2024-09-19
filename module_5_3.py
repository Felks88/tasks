class House:
    def __init__(self, name, number_of_floors):  # исправлено
        self.name = name
        self.number_of_floors = number_of_floors

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
            return self.number_of_floors == other.number_of_floors  #Дополнено
        else:
            print('None')

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)  #Дополнено
        else:
            print('None')

    def __iadd__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)  #Дополнено
        else:
            print('None')

    def __radd__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)  #Дополнено
        else:
            print('None')

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors  #Дополнено
        else:
            print('None')

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors   #Дополнено
        else:
            print('None')

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors  #Дополнено
        else:
            print('None')

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors  #Дополнено
        else:
            print('None')

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors  #Дополнено
        else:
            print('None')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
