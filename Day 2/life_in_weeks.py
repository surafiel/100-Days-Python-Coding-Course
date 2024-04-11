your_age = int(input("How old are you? "))

ninety_wks = 90 * 52
your_age_in_wks = your_age * 52

wks_left = ninety_wks - your_age_in_wks
print(f"You have {wks_left} weeks left")