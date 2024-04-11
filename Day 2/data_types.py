two_digit_number = input("Pick a two digit number: ")

if len(two_digit_number) == 2:
    digit_sum = int(two_digit_number[0]) + int(two_digit_number[1])
    print(digit_sum)
else:
    print("Please give a two digit number")