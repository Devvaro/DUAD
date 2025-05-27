class BankAccount():
    def __init__(self, balance=0):
        self.balance = balance

    def insert_money(self):
        insert = int(input("Insert and amount of money: "))
        self.balance += insert
        print(f'your current balance is ${self.balance}')
    

    def withdraw_money(self):
        withdraw = int(input("Insert and amount of money: "))
        if self.balance - withdraw < 0:
            print("Insufficient funds! You cannot withdraw this amount.")
        else:
            self.balance -= withdraw 
            print(f'your current balance is ${self.balance}')


class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=20):
        super().__init__(balance)
        self.min_balance = min_balance
        
    def withdraw_money(self):
        withdraw = int(input("Insert and amount of money: "))
        if self.balance - withdraw < self.min_balance:
            print(f"You can't withdraw this amount because your balance cannot go below ${self.min_balance}.")
        else:
            self.balance -= withdraw 
            print(f'your current balance is ${self.balance}')


my_bank_account=SavingsAccount()

while True:
    menu=input("type 1 to insert money or type 2 to withdraw money (or type 'exit' to quit): ").strip()

    if menu == "1":
        my_bank_account.insert_money()
    elif menu == "2":
        my_bank_account.withdraw_money()
    elif menu.lower()== "exit":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid input. Please type 1, 2, or 'exit'.")