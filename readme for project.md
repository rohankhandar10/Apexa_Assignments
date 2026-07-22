# 🏦 Threaded Bank Transaction System

A Python project that demonstrates **multithreading and synchronization** by simulating concurrent bank transactions. Multiple threads perform deposit and withdrawal operations safely using `threading.Lock` to prevent race conditions.

---

## 📌 Features

- Multi-threaded deposit and withdrawal operations
- Thread-safe balance updates using `threading.Lock`
- Prevents race conditions
- Handles insufficient balance gracefully
- Displays real-time transaction logs
- Calculates the final account balance after all transactions

---

## 🛠️ Technologies Used

- Python 3.x
- threading module
- time module

---

## 📂 Project Structure

```
Threaded-Bank-Transaction/
│── bank_transaction.py
│── README.md
```

---

## ▶️ How It Works

1. A bank account is initialized with a starting balance.
2. One thread repeatedly deposits money.
3. Two threads simultaneously withdraw money.
4. A lock ensures only one thread accesses the balance at a time.
5. The program prints all transactions and the final balance.

---

## 🚀 How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/Threaded-Bank-Transaction.git
```

2. Navigate to the project folder

```bash
cd Threaded-Bank-Transaction
```

3. Run the program

```bash
python bank_transaction.py
```

---

## 📸 Sample Output

```
Deposit Thread deposited ₹200 | Balance: ₹1200
Withdraw Thread 1 withdrew ₹150 | Balance: ₹1050
Withdraw Thread 2 withdrew ₹300 | Balance: ₹750
...
Withdraw Thread 2 failed to withdraw ₹300 (Insufficient Balance)

Final Account Balance: ₹50
```

> Note: The transaction order and final balance may vary because thread scheduling is handled by the operating system.

---

## 🔒 Thread Synchronization

The project uses:

```python
threading.Lock()
```

This ensures that only one thread can modify the account balance at a time, preventing race conditions and maintaining data consistency.

---

## 📚 Concepts Demonstrated

- Multithreading
- Thread Synchronization
- Mutual Exclusion (Mutex)
- Race Condition Prevention
- Critical Section
- Object-Oriented Programming (OOP)
- Concurrent Programming

---

## 🎯 Learning Outcomes

After completing this project, you will understand:

- How Python threads work
- Creating and managing threads
- Using `threading.Lock`
- Synchronizing shared resources
- Preventing race conditions
- Building concurrent applications

---

## 👨‍💻 Author

**Rohan Khandar**

Third Year Electronics & Telecommunication Engineering (EXTC)

Shri Sant Gajanan Maharaj College of Engineering, Shegaon

---

## 📄 License

This project is open source and available under the MIT License.
