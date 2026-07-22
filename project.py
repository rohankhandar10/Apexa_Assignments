import threading
import time

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    # Deposit method
    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"{threading.current_thread().name} deposited ₹{amount} | Balance: ₹{self.balance}")

    # Withdraw method
    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"{threading.current_thread().name} withdrew ₹{amount} | Balance: ₹{self.balance}")
            else:
                print(f"{threading.current_thread().name} failed to withdraw ₹{amount} (Insufficient Balance)")

# Function for deposit thread
def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)
        time.sleep(0.1)

# Function for withdrawal thread
def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)
        time.sleep(0.1)

# Main Program
account = BankAccount(1000)

t1 = threading.Thread(target=deposit_task, args=(account, 200), name="Deposit Thread")
t2 = threading.Thread(target=withdraw_task, args=(account, 150), name="Withdraw Thread 1")
t3 = threading.Thread(target=withdraw_task, args=(account, 300), name="Withdraw Thread 2")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("\nFinal Account Balance: ₹", account.balance)