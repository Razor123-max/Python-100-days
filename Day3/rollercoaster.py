print("\nWelcometo the rollercoaster!!!\n")
print

height = int(input("What is your height in cm? "))

if height >= 130:
    print("\nCongratulations! You are eligible to ride the rollercoaster.\n")

    age = int(input("How old are you? "))
    if age <=12:
        print("\nYou have to pay 5$\n")
    elif age >= 17:
        print("\nYou have to pay 7$\n")

    else:("\nYou have to pay 5$\n")

else:
    print("\nSorry, you need to grow a little bit taller before you can ride the rollercoaster")