class BankAccount:

    def __init__(self, Holder_Name,Balance):
        self.Holder_Name = Holder_Name
        self.Balance = Balance

    def show_balance(self):
        print("Current Balance:",self.Balance)

    def deposit(self,Amount):
        if Amount > 0:
            self.Balance += Amount
        else:
            print("Insufficient Amount")

    def withdraw(self, Amount):
        if Amount <= self.Balance:
            self.Balance -= Amount
            print(Amount,"Withdrawn Successfully")

        else:
            print("Insufficient Balance")


acc1 = BankAccount("Kushal",1000)

acc1.show_balance()

acc1.deposit(500)
acc1.show_balance()

acc1.withdraw(700)
acc1.show_balance()

acc1.withdraw(5000)
acc1.show_balance()

acc1.deposit(-700)
acc1.show_balance()
