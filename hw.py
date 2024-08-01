import threading
import time

class BankAccount():
    def __init__(self):
        self.balance = 1000

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, new balance is {self.balance}')

    def withdraw(self, amount):
        self.balance -= amount
        print(f'withdrew {amount}, new balance is {self.balance}')
def deposit_task(account, amount):
    threading.Lock().acquire()
    for _ in range(5):
        account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)
    time.sleep(0.000001)
    try:
        threading.Lock().release()
    except:
        pass

account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
threading.Lock().acquire()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
