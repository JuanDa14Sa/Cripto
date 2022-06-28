import datetime


class Transaction:
    def __init__(self, sender, reciever, amount):
        self.sender = sender
        self.reciever = reciever
        self.amount = amount
        self.timestamp = datetime.datetime.now()
        self.sender.wallet -= amount
        self.reciever.wallet += amount
        self.sender.transactions.append(self)
        self.reciever.transactions.append(self)
    def display_transaction(self):
        print("Sender: " + self.sender.name)
        print("Reciever: " + self.reciever.name)
        print("Amount: " + str(self.amount))
        print("Timestamp: " + str(self.timestamp))
        print("\n")
    def display_sender_transactions(self):
        print("Sender: " + self.sender.name)
        print("Amount: " + str(self.amount))
        print("Timestamp: " + str(self.timestamp))
        print("\n")
    