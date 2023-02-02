#Write a program to print the sum of all the digits in the given number.
number = int(input())
number_string = str(number)

sum = 0
for each_digit in number_string:
    sum += int(each_digit)
    
print(sum)