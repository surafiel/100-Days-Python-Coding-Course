print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much would you like to give? 10, 12, or 15? "))
count = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip = bill * tip_as_percent
total_bill = bill + total_tip
payment = total_bill / count
final_payment = round(payment, 2)
final_payment = "{:.2f}".format(payment)

print(f"Each person should pay: ${final_payment}")
