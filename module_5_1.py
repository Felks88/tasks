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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
