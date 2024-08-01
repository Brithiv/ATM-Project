import sys
class customer:
    bank = 'Indian Bank'
    def __init__(self, balance):
        self.balance = balance
    def display(self,pin):
        if pin == 1234:
            print('D-Deposit, W-Withdraw, C-Cancel')
            choice = input('Enter your choice: ')
            if choice == 'D':
                self.deposit(amount=0, total=0)
            elif choice == 'W':
                self.withdraw(amount=0,total=0)
            elif choice == 'C':
                self.cancel()
        else:
            print('you have entered an Incorrect Pin')

    def deposit(self,amount, total):
        amount = int(input('Enter the amount: '))
        self.balance+= amount
        total = print('Your avaliable balance is: ',self.balance)
        print('Do you wish to continue')
        print('Y-Yes, N-No')
        Option = input('Enter your Option: ')
        if Option == 'Y':
            self.display(pin=1234)
        elif Option == 'N':
            self.cancel()

    def withdraw(self, amount, total):
        amount = int(input('Enter the amount: '))
        if self.balance<amount:
            print('Insufficient Balance')
            print('Thank you have a Nice Day')
        else:
            self.balance -= amount
            total = print('Your avaliable balance is: ', self.balance)
            print('Do you wish to continue')
            print('Y-Yes, N-No')
            Option = input('Enter your Option: ')
            if Option == 'Y':
                self.display(pin=1234)
            elif Option == 'N':
                self.cancel()

    def cancel(self):
        print('Thank you have a Nice DAy')
        sys.exit()

print('Welcome to',customer.bank)
customer1 = customer(balance=0)
customer1.display(int(input('Enter your Pin: ')))