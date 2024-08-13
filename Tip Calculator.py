print("\nWelcome to tip calculator!\n")

total_bill = int(input("What was the total bill?\n"))

tip = int(input("How much tip would you like to give?\n 10, 12 or 15?\n"))

tip_amount = (total_bill * (tip / 100) + total_bill)

split = int(input("How many people to split the bill?\n"))
split_amount = round(tip_amount / split, 2)

print(f"Each person should pay:{split_amount}\n")
