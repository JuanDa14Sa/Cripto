from Transaction import Transaction



class User:
    def __init__(self, name, wallet=5):
        self.name = name # Identificador del usuario
        # self.balance = True # Si el usuario está debiendo 
        self.wallet = wallet # Cantidad de monedas que tiene el usuario
        # self.transactions = []

    def submit_transaction(self, amount, reciever):
        trnsact=Transaction(self.name, reciever, amount)
        if self.wallet >= amount:
            self.wallet -= amount
            reciever.wallet += amount
            # self.transactions.append(amount)
            return trnsact
        else :
            print("Not enough money")
            return None

    def mine_block(self,block, solved_proof):
        if block.test_problem(solved_proof):
            block.add_transaction(Transaction(User('PHILIP GOD',wallet=1000000000),self, 0.5)) # 0.5 es la recomenpensa por minar un bloque
            self.wallet += 0.5
            return True
        else:
            return False

    # def make_withdrawal(self, amount):
    #     self.balance -= amount
    #     self.transactions.append(amount)
    #     return self.balance

    def display_user_wallet(self):
        print("User: " + self.name)
        # print("Balance: " + str(self.balance))
        print("Wallet: " + str(self.wallet))

    def display_user_transactions(self):
        print("User: " + self.name)
        print("Transactions")