import threading
import time
import random

lock = threading.Lock()


class Bank(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.balance = 0
        self.lock = lock

    def deposit(self):
        for i in range(100):
            x = random.randint(50, 500)
            self.balance += x
            print(f'Пополнение: {x}. Баланс: {self.balance}.')
            if self.balance >= 500 and lock.locked():
                lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            x = random.randint(50, 500)
            print(f'Запрос на {x}')
            if x <= self.balance:
                self.balance -= x
                print(f'Снятие: {x}. Баланс: {self.balance}.')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                lock.acquire()
            

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
