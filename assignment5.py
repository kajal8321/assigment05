# Challenge 1: Square Numbers and Return Their Sum
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2

# Example usage
point = Point(1, 3, 5)
result = point.sqSum()
print(result)  # Output: 35

# Challenge 2: Implement a Calculator Class
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num2 / self.num1

# Example usage
obj = Calculator(10, 94)
print(obj.add())       # Output: 104
print(obj.subtract())  # Output: 84
print(obj.multiply())  # Output: 940
print(obj.divide())    # Output: 9.4


# Challenge 3: Implement the Complete Student Class

class Student:
    def __init__(self):
        self._name = None
        self._rollNumber = None

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setRollNumber(self, rollNumber):
        self._rollNumber = rollNumber

    def getRollNumber(self):
        return self._rollNumber

# Example usage
student = Student()
student.setName("John")
student.setRollNumber("12345")
print(student.getName())        # Output: John
print(student.getRollNumber())   # Output: 12345

# Challenge 4: Implement a Banking Account

class Account:
    def __init__(self, title=none, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal_amount(self, amount):
            balance=2000
            withdrawal(500)
            getbalance()
        

     def deposit(self, amount):
            balance=2000
            deposit(500)
            getBalance()

             
    def getBalance(self):
        balance=0
        getbalance()

class savingsAccount(Account):
    def_init_(self, title=none, balance=0, interestRate=0):
    super()._init_(title, balance)
    self.interestRate = interestRate


    def interestAmount(self):
        balance=2000
        interestRate=5
        interestAmoun()

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate()

# Example usage
account = Account("Ashish", 5000)
print(account.title)  # Output: Ashish
print(account.balance)  # Output: 5000

savings_account = SavingsAccount("Ashish", 5000, 5)
print(savings_account.title)  # Output: Ashish
print(savings_account.balance)  # Output: 5000
print(savings_account.interestRate)  # Output: 5


