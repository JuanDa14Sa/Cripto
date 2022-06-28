class User:
    def __init__(self, name, wallet=5):
        self.name = name # Identificador del usuario
        # self.balance = True # Si el usuario está debiendo 
        self.wallet = wallet # Cantidad de monedas que tiene el usuario
        # self.transactions = []

    def submit_transaction(self, amount, reciever):
        trnsact=Transaction()
        if self.wallet >= amount:
            self.wallet -= amount
            reciever.wallet += amount
            # self.transactions.append(amount)
            return True

    def make_withdrawal(self, amount):
        self.balance -= amount
        self.transactions.append(amount)
        return self.balance

    def display_user_balance(self):
        print("User: " + self.name)
        print("Balance: " + str(self.balance))
        print("Transactions: " + str(self.transactions))

    def display_user_transactions(self):
        print("User: " + self.name)
        print("Transactions         