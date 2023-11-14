class User:
    def __init__(self, username, email_address):
        self.name = username
        self. email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdraw(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"{self.name}'s balance is now ${self.account_balance}")

    def transfer_money(self, other_user, amount):
        if amount <= self.account_balance:
            self.make_withdraw(amount)
            other_user.make_deposit(amount)
            print(f"{self.name} transferred ${amount} to {other_user.name}")
        else:
            print(f"{self.name} does not have sufficient funds to transfer ${amount}")


#creating instances of the User Class 
guido = User("Guido Van Rossume", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

# print(guido.name)
# print(monty.name)

#Making deposits and withdrawals
guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(2000)
monty.make_deposit(50)

guido.make_withdraw(70)
monty.make_withdraw(20)

guido.transfer_money(monty, 200)
monty.transfer_money(guido, 200)

# Displaying user balances
guido.display_user_balance()
monty.display_user_balance()