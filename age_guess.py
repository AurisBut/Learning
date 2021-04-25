def guess_my_age(actual_age):
    keep_trying = True
    tries = 0

    while keep_trying:

        tries += 1
        print(f"Try number: {tries}")

        guessed_age = int(input("How old am I? "))

        if guessed_age == actual_age:
            if tries == 1:
                print("Congratulations, you guessed my age on your first try!")
            else:
                print(f"Nice, you guessed my age after {tries} tries.")
            keep_trying = False

        else:
            if guessed_age > actual_age:
                print(f"Sorry, I am younger than {guessed_age}.")
            else:
                print(f"Sorry, I am older than {guessed_age}.")

            keep_trying = input('Try again? (Y/N) ').upper() == "Y"


guess_my_age(14)