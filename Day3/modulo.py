#check if the entered number is even or odd

number = int(input("Enter the number you want to check if it is even or odd"))

if number % 2 == 0:
    print(f"The number {number} is even")

else:
    print(f"The number {number} is odd")