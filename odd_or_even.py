def even():
    while True:
        number = int(input('Enter number: '))
        if number % 2 == 0:
            print('Number is even')
        else:
            print('Number is odd')
        kartojimas = input('Want to try different number? (Y/N)- ').upper()
        if kartojimas == 'Y':
            even()
        else:
            print('Thanks for checking')
            break

even()
