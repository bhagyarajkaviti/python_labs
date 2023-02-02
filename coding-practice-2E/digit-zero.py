#Write a program that reads a three-digit number and checks if the given number contains 0.
number = int(input())
three_digit_number = str(number)
three_digit_number_condition = len(three_digit_number) == 3

result = (three_digit_number[0] == "0") or (three_digit_number[1] == "0") or (three_digit_number[2] == "0")
print(result)