"""
For this challenge, create a bank account class that has two attributes:
    owner
    balance

and two methods:
    deposit
    withdraw

As an added requirement, withdrawals may not exceed the available balance.
Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""

class Account():
    def __init__(self, own, bal=0):
        self.own = own
        self.bal = bal
        # print(f'Account owner: {own}')
        # print(f'Account balance: {bal}')

    def __str__(self):
        return f"""
        Account owner is: {self.own}
        Account balance is: {self.bal}"""

    def owner(self):
        return 'Account owner is: ' + self.own

    def balance(self):
        return 'Account balance is: ' + str(self.bal)

    def deposit(self):
        amount = float(input('\nHow much do you want to deposit: '))
        self.bal += amount
        print(' Amount Deposited:', amount)
        print(' Current account balance is: {}'.format(self.bal))

    def withdraw(self):
        question = input('\nDo you want to withdraw? Y or N? ').upper()
        if question in ['Y', 'YES']:
            amount = float(input('Enter amount to withdraw: '))
            if self.bal >= amount:
                self.bal -= amount
                print('\n You have withdrew: ', amount)
                print(' Your remaining balance is: {}'.format(self.bal))
                print('Have a nice day!')
            else:
                print('\n Insufficient balance!')
                amount = float(input(' Please enter different amount which is lower or equal to {}: '.format(self.bal)))
                if amount >= self.bal:
                    self.bal -= amount
                    print('\n You have withdrew: ', amount)
                    print(' Your remaining balance is: {}'.format(self.bal))
                    print(' Have a nice day!')
                else:
                    print('\n Insufficient balance!')
                    print(' Have a nice day!')
        else:
            print('Have a nice day!')

acc = Account('Aurimas', 1000)

print(acc)
acc.deposit()
acc.withdraw()
