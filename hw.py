import queue
import threading
from time import sleep

class Customers(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number

class Table:
    def __init__(self, number):
        self.number = int(number)
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = list(tables)
        self.number = 1

    def customer_arrival(self):
        x = 0
        for _ in range(20):
            print(f'Клиент номер {self.number} прибыл')
            self.queue.put(Customers(self.number))
            sleep(1)
            self.number += 1
            threading.Thread(target=cafe.serve_customer).start()
    def serve_customer(self):
        while True:
            for i in self.tables:
                if i.is_busy == False:
                    x = self.queue.get()
                    i.is_busy = True
                    sleep(0.01)
                    print(f'Клиент номер {x.number} сел за стол {i.number}')
                    sleep(5)
                    print(f'Клиент номер {x.number} покушал и ушел')
                    i.is_busy = False



table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]
cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
