import random


def maisymas(stringas):
    stringas = list(stringas)
    random.shuffle(stringas)
    password = ''.join(stringas)
    return password

# Didziuju raidziu generacija
didzioji1 = chr(random.randint(65, 90))
didzioji2 = chr(random.randint(65, 90))

# Mazuju raidziu generacija
mazoji1 = chr(random.randint(97, 122))
mazoji2 = chr(random.randint(97, 122))

# Skaiciu generacija

skaicius1 = str(random.randint(1, 9))
skaicius2 = str(random.randint(1, 9))

# Simboliu generacija

simbolis1 = chr(random.randint(33, 47))
simbolis2 = chr(random.randint(33, 47))

# Slaptazodzio generacija

password = didzioji1 + didzioji2 + mazoji1 + mazoji2 + skaicius1 + skaicius2 + simbolis1 + simbolis2
password = maisymas(password)

print(didzioji2, didzioji1, mazoji1, mazoji2, skaicius1, skaicius2, simbolis1, simbolis2)
print(password)



