import random


def ilgumas():
    ilgis = int(input('Keliu simboliu slaptazodis? [8,10 ar 12]? - '))
    if ilgis == 8:
        return f'Jusu 8 simboliu slaptazodis yra: {generacija_a()}'
    elif ilgis == 10:
        return f'Jusu 10 simboliu slaptazodis yra: {generacija_b()}'
    elif ilgis == 12:
        return f'Jusu 12 simboliu slaptazodis yra: {generacija_c()}'
    else:
        print('Slaptazodi turi sudaryti 8, 10 arba 12 simboliu')
        ilgis2 = int(input('Keliu simboliu slaptazodis? [8,10 ar 12]? - '))
        if ilgis2 == 8:
            return f'Jusu 8 simboliu slaptazodis yra: {generacija_a()}'
        elif ilgis2 == 10:
            return f'Jusu 10 simboliu slaptazodis yra: {generacija_b()}'
        elif ilgis2 == 12:
            return f'Jusu 12 simboliu slaptazodis yra: {generacija_c()}'
        else:
            return 'Neskaitote salygos!'

def maisymas(stringas):
    stringas = list(stringas)
    random.shuffle(stringas)
    password = ''.join(stringas)
    return password

def generacija_a():
    didzioji1 = chr(random.randint(65, 90))
    didzioji2 = chr(random.randint(65, 90))
    mazoji1 = chr(random.randint(97, 122))
    mazoji2 = chr(random.randint(97, 122))
    skaicius1 = str(random.randint(1, 9))
    skaicius2 = str(random.randint(1, 9))
    simbolis1 = chr(random.randint(33, 47))
    simbolis2 = chr(random.randint(33, 47))
    password = didzioji1 + didzioji2 + mazoji1 + mazoji2 + skaicius1 + skaicius2 + simbolis1 + simbolis2
    password = maisymas(password)
    return password

def generacija_b():
    didzioji1 = chr(random.randint(65, 90))
    didzioji2 = chr(random.randint(65, 90))
    didzioji3 = chr(random.randint(65, 90))
    mazoji1 = chr(random.randint(97, 122))
    mazoji2 = chr(random.randint(97, 122))
    skaicius1 = str(random.randint(1, 9))
    skaicius2 = str(random.randint(1, 9))
    skaicius3 = str(random.randint(1, 9))
    simbolis1 = chr(random.randint(33, 47))
    simbolis2 = chr(random.randint(33, 47))
    password = didzioji1 + didzioji2 + didzioji3 + mazoji1 + mazoji2 + skaicius1 + skaicius2 + skaicius3 + simbolis1 + simbolis2
    password = maisymas(password)
    return password

def generacija_c():
    didzioji1 = chr(random.randint(65, 90))
    didzioji2 = chr(random.randint(65, 90))
    didzioji3 = chr(random.randint(65, 90))
    mazoji1 = chr(random.randint(97, 122))
    mazoji2 = chr(random.randint(97, 122))
    mazoji3 = chr(random.randint(97, 122))
    skaicius1 = str(random.randint(1, 9))
    skaicius2 = str(random.randint(1, 9))
    skaicius3 = str(random.randint(1, 9))
    simbolis1 = chr(random.randint(33, 47))
    simbolis2 = chr(random.randint(33, 47))
    simbolis3 = chr(random.randint(33, 47))
    password = didzioji1 + didzioji2 + didzioji3 + mazoji1\
               + mazoji2 + mazoji3 + skaicius1 + skaicius2\
               + skaicius3 + simbolis1 + simbolis2 + simbolis3
    password = maisymas(password)
    return password

print(ilgumas())