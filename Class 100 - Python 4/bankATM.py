class atm(object):
    def __init__ (self, card_number, pin):
        self.card_number = card_number
        self.pin = pin

    def CashWithdrawl(self):
        ask = int(input("How much would you like to withdraw: "))
        print(ask)

    def Balance(self):
        print("You have 50,000")

new_user = atm("01052010","1521")
print(new_user.Balance())