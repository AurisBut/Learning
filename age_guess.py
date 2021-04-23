class Age:
    def __init__(self, tries=0):
        self.tries = tries
        self.my_age = 14
        self.tries = 1

    def guess(self):

        number = int(input('How old I am?- '))
        if number == self.my_age:
            print('')
            print(f'Congratulations, you guessed it in {self.tries} tries!')
        else:
            if number > self.my_age:
                print(f'\nTry no.: {self.tries}')
                self.tries += 1
                print(f'|-- Incorrect. I am younger than {number} --|')
                repeat = input('Try once again? (Y/N)- ').upper()
                if repeat == 'Y':
                    self.guess()
                else:
                    pass
            elif number < self.my_age:
                print(f'\nTry no.: {self.tries}')
                self.tries += 1
                print(f'|-- Incorrect. I am older than {number} --|')
                repeat = input('Try once again? (Y/N)- ').upper()
                if repeat == 'Y':
                    self.guess()
                else:
                    pass


x = Age(1)
x.guess()
