class Card:
    def __init__(self,balance):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self._balance:
            print("Denied: insufficient funds.")
            return False
        self._balance -= amount
        print (f"Dispensive ¥{amount}. Remaining : ¥ {self._blalance}")
        return True

    def check_balance(self):
        return self._balance


def main():
    card = Card(5000)
    print (f"Welcome. Your balance is ¥{card.check_balance()}.")

    while True:
        amount = int (input ("Enter amount ot withdraw (0 to exit):"))
        if amount == 0:
            print (f" Goodbuy. Final balance: ¥{ card.check_balance()}")
            break
        card.withdraw(amount)

if __name__=="__main__":
    main()