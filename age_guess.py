def number_guess():
    number = int(input('Kiek man metu? '))
    ernesto_amzius = 14
    tries = 1

    while True:
        if number == ernesto_amzius:
            print('')
            print('Sveikinu, atspejai!')
            print(f'Atspejai is {tries} karto')
            break
        else:
            print('')
            print('Neatspejai mano amziaus')
            question = input('Ar nori bandyti dar? (T/N) ').upper()
            if question in ['T', 'TAIP', 'TEIP', 'Y', 'YES']:
                tries += 1
                print(f'Jau spejai {tries} kartus')
                number = int(input('Kiek man metu? '))
                continue
            else:
                print(f'Atspejai is {tries} karto')
                break


number_guess()
