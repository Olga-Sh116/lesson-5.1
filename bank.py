class Account:
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Вы успешно пополнили счёт. Сумма на счете - {self.balance}.")


    def withdraw(self, amount):
        if amount > self.balance:
           print(f"Недостаточная сумма на счете")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"Вы успешно сняли {amount} рублей. Остаток на счёте: {self.balance}")



    def all_balance(self):
        print(f"Текущий баланс - {self.balance}")

man = Account("12323132", 600)

man.all_balance()
man.withdraw(450)
man.withdraw(800)
man.deposit(3566)



