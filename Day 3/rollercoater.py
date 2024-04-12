print("Welcome to the rollercoaster!")
cm = int(input("To be able to ride, you have to be 120 cm tall. How tall are you in cm? "))
age = int(input("Tell me your age so I can give you the right price? "))

if cm > 120:
    if 18 < age < 45:
        print("Your ticket is $12.")
    elif 12 <= age <= 18:
        print("Your ticket is $7")
    elif 45 < age < 55:
        print("Your ticket is free!")
    elif age < 12:
        print("Your ticket is $5.")
else:
    print("Sorry, you have to be taller to ride the rollercoaster!")

photo = input("Would you like to take some photos? (Y / N)")
if photo == "Y" and cm > 120 and age < 45:
    if 18 < age < 45:
        print("That'll be $3 extra dollars, the total bill will be $15.")
    elif 12 <= age <= 18:
        print("That'll be $3 extra dollars, the total bill will be $10.")
    elif age < 12:
        print("That'll be $3 extra dollars, the total bill will be $8.")
else:
    False
    