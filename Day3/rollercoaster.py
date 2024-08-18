print("\nWelcometo the rollercoaster!!!\n")

height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("\nCongratulations! You are eligible to ride the rollercoaster.\n")

    age = int(input("How old are you? "))

    if age <=12:
        bill = 5
        print("\nChil tickets are $5\n")

    elif age >= 17:
        bill = 7
        print("\nYouth tickets are $7\n")

    else:
        bill = 12
        ("\nAdult tickets are $12\n")
    

    wants_photo = input("Do you want to have a photo taken?\n $3 for a photo\n Type y for Yes and n for No\n")
    if  wants_photo == "y":
        bill += 3
        print(f"Your total bill is {bill}")


else:
    print("\nSorry, you need to grow a little bit taller before you can ride the rollercoaster")