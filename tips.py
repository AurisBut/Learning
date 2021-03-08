bill = int(input('Kokio dydzio saskaita?- '))
people = int(input('Kiek zmoniu valge?- '))
tips = int(input('Kiek % arbatpinigiu paliksite?- '))

def twenty_tip():
    tip = bill * tips * 0.01
    each = tip / people
    each_rounded = round(each)
    print(f'\n\t{tips}% arbatpinigiai nuo {bill} EUR sumos butu {tip} EUR')
    print(f'\tKiekvienas turi moketi po {each_rounded} EUR')

twenty_tip()