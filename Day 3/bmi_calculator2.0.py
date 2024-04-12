print("Welcome to the BMI Calculator 2.0")
height = float(input("What is your height in meters? "))
weight = int(input("How much do you weigh in kg? "))

BMI = weight // (height ** 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI} and you are underweight.")
if 18.5 < BMI < 25:
    print(f"Your BMI is {BMI} and you have a normal weight.")
if 25 < BMI < 30:
    print(f"Your BMI is {BMI} and you are slightly overweight.")
if 30 < BMI < 35:
    print(f"Your BMI is {BMI} and you are obese.")
if BMI > 35:
    print(f"Your BMI is {BMI} and you are clinically obese.")
