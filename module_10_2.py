import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        opponents = 100
        days = 0
        print(f'{self.name}, на нас напали!')
        while opponents > 0:
            opponents -= self.power
            days += 1
            sleep(1)
            print(f'{self.name} сражается {days}, осталось {opponents} воинов.''\n')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончены!')