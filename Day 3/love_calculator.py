print("The love calculator will calculate your score based off the couple names...")
name1 = input("What is the first person's name? ")
name2 = input("What is the second person's name? ")

combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

first_digit = str(first_digit)
second_digit = str(second_digit)
score = first_digit + second_digit
score = int(score)

if score < 10 or score > 90:
    print(f"Your score is {score} almost like y'all are coke and mentos!")
elif 40 <= score <= 50:
    print(f"Your score is {score} which is probably why you guys would be such a great couple!")
else:
    print(f"Your score is {score}...")
