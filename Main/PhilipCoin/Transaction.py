import datetime
# from User import User

class Transaction:
    def __init__(self, sender, reciever, amount):
        self.sender = sender
        self.reciever = reciever
        self.amount = amount
        self.timestamp = datetime.datetime.now()

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
    