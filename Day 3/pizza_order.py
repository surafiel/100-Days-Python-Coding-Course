print("Thank you for choosing the world-renowned Python Pizza!")

pizza = input("What size pizza would you like? (S), (M), or (L)? ")
pepperoni = input("Would you like to add pepperoni? (Y / N) ")
cheese = input("Would you like extra cheese on your pizza? (Y / N)? ")

if pizza == "S":
    if pepperoni == "Y":
        if cheese == "Y":
            print("Your final bill is $18")
        else:
            print("Your final bill is $17")
    else:
        if cheese == "Y":
            print("Your final bill is $16")
        else:
            print("Your final bill is $15")

elif pizza == "M":
    if pepperoni == "Y":
        if cheese == "Y":
            print("Your final bill is $24")
        else:
            print("Your final bill is $23")
    else:
        if cheese == "Y":
            print("Your final bill is $21")
        else:
            print("Your final bill is $20")

else:
    if pepperoni == "Y":
        if cheese == "Y":
            print("Your final bill is $29")
        else:
            print("Your final bill is $28")
    else:
        if cheese == "Y":
            print("Your final bill is $26")
        else:
            print("Your final bill is $25")
