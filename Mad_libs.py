def istorija_m():
    print('Istorija Moteris')


def istorija_mv():
    print('Istorija moteris su vaikais')


def istorija_v():
    print('Istorija vyras')


vardas = input('Koks tavo vardas?- ')
try:
    age = int(input('Kiek tau metų?- '))
except ValueError:
    print('Amžių rašykite skaičiais!')
miestas = input('Iš kokio tu miesto?- ')
vaikai = input('Ar turite vaikų? (T/N)- ').upper()
if vaikai == 'T':
    vaiku_kiekis = int(input('Iveskite vaikų skaičių: '))
else:
    vaiku_kiekis = 0
lytis = input('Tu moteris (M) ar vyras (V)?- ').upper()
if lytis == 'M' and vaiku_kiekis == 0:
    istorija_m()
elif lytis == 'M' and vaiku_kiekis > 0:
    istorija_mv()
else:
    istorija_v()
