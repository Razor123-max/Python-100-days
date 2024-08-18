print("\nWelcometo the rollercoaster!!!\n")

height = int(input("What is your height in cm? "))

if height >= 120:
    print("\nCongratulations! You are eligible to ride the rollercoaster.\n")

    age = int(input("How old are you? "))
    if age <=12:
        print("\nChil tickets are $5\n")
    elif age >= 17:
        print("\nYouth tickets are $7\n")

    else:("\nAdult tickets are $12\n")

else:
    print("\nSorry, you need to grow a little bit taller before you can ride the rollercoaster")