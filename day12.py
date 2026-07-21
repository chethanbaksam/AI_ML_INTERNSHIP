class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def display(self):
        print("Owner:", self.owner)
        print("Balance:", self.balance)


acc1 = Account("Chethan", 5000)
acc1.display()

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


class SavingsAccount(Account):
    pass


acc = SavingsAccount("Chethan", 5000)

print(acc.owner)
print(acc.balance)

print()

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


class SavingsAccount(Account):
    def calculate_interest(self):
        interest = self.balance * 0.05
        print("Interest:", interest)


acc = SavingsAccount("Chethan", 10000)

acc.calculate_interest()

print()

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate


acc = SavingsAccount("Chethan", 10000, 5)

print(acc.owner)
print(acc.balance)
print(acc.interest_rate)

print()

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print("Balance:", self.balance)


class SavingsAccount(Account):
    def add_interest(self):
        self.balance += self.balance * 0.05


acc = SavingsAccount("Chethan", 10000)

acc.show_balance()

acc.add_interest()

acc.show_balance()

print()

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def display(self):
        print("Owner:", self.owner)
        print("Balance:", self.balance)


class SavingsAccount(Account):
    def calculate_interest(self):
        interest = self.balance * 0.05
        print("Interest Earned:", interest)


acc = SavingsAccount("Chethan", 20000)

acc.display()
acc.calculate_interest()