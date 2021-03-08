def number_guess():
    number = int(input('What number are you thinking? '))
    tries = 1
    while True:
        if number % 2 == 0:
            print('')
            print('This is even number')
            question = input('Want to try again? (Y/N) ').upper()
            if question in ['Y', 'YES']:
                tries += 1
                number = int(input('What number are you thinking? '))
                continue
            else:
                print(f'You had {tries} tries')
                break
        else:
            print('')
            print('This is odd number')
            question = input('Want to try again? (Y/N) ').upper()
            if question in ['Y', 'YES']:
                tries += 1
                number = int(input('What number are you thinking? '))
                continue
            else:
                print(f'You had {tries} tries')
                break


number_guess()
