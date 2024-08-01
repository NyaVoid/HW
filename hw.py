import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100
        self.score = 0

    def run(self):
        while self.enemies > 0:
            self.score += 1
            time.sleep(1)
            self.enemies -= self.power
            print(f'{self.name} сражается {self.score} день(дня)..., осталось {self.enemies} воинов.')
        print(f'{self.name} одержал победу спустя {self.score} день(дня)')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
time.sleep(0.01)
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились')
