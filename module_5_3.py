class House:
    def __init__(self, neme, number_of_floors):
        self.name = neme
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
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        return House(self.name, self.number_of_floors + value)

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

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
