def istorija_m():
    print('\t \n Sveiki, aš ' + vardas + '. Man yra ' + amzius +
          ' metai. \n Vaikų neturiu. Esu kilusi iš ' + miestas + '.')


def istorija_mv():
    if vaiku_kiekis == '1':
        print('\t \n Sveiki, aš ' + vardas + '. Man yra ' + amzius +
              ' metai. \n Turiu ' + vaiku_kiekis + ' vaiką. Esu kilusi iš ' + miestas + '.')
    else:
        print('\t \n Sveiki, aš ' + vardas + '. Man yra ' + amzius +
              ' metai. \n Turiu ' + vaiku_kiekis + ' vaikus. Esu kilusi iš ' + miestas + '.')


def istorija_v():
    print('\t \n Sveiki, aš ' + vardas + '. Man yra ' + amzius +
              ' metai. \n Vaikų neturiu. Esu kilęs iš ' + miestas + '.')


vaiku_skaicius = ['1', '2', '3', '4', '5']
vardas = input('Koks tavo vardas?- ')
amzius = input('Kiek tau metų?- ')
miestas = input('Iš kokio tu miesto?- ')
vaikai = input('Ar turite vaikų? (T/N)- ').upper()
if vaikai == 'T':
    vaiku_kiekis = input('Iveskite vaikų skaičių: ')
else:
    vaiku_kiekis = '0'
lytis = input('Tu moteris (M) ar vyras (V)?- ').upper()
if lytis == 'M' and vaiku_kiekis == '0':
    istorija_m()
elif lytis == 'M' and vaiku_kiekis in vaiku_skaicius:
    istorija_mv()
else:
    istorija_v()
