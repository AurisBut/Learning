print('|-- TIPS CALCULATOR --|')

bill = float(input('How much to pay?- '))
people = int(input('How many people ate?- '))
tips = int(input('What % of tip will you leave?- '))

def twenty_tip():
    tip = bill * tips * 0.01
    each = tip / people + 1
    each_rounded = round(each)
    print(f'\n\t{tips}% tip of {bill} EUR will be {round(tip, 2)} EUR')
    print(f'\tEveryone has to pay {each_rounded} EUR')

twenty_tip()