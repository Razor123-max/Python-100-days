print("\nWelcome to Python Pizza Deliveries!\n")

bill = 0

size = input("What size of pizz do you want? S, M or L:\n")

if size == "S":
    bill += 15

elif size == "M":
    bill += 20

elif size == "L":
    bill += 25

pepperoni = input("\nDo you want pepperoni on your pizza? Y or N:\n")

if pepperoni == "Y" and size == "S":
    bill += 2

elif pepperoni == "Y" and (size == "M" or size == "L"):
    bill += 3

extra_cheese = input("\nDo you want extra cheese? Y or N:\n")

if extra_cheese == "Y":
    bill += 1

print(f"\nThank you for your order! Your total bill is ${bill}.")