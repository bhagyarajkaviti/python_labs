#Given a string, write a program to return the sum and average of the digits of all numbers that appear in the string, ignoring all other characters.
#Input:
#The input will be a single line containing a string.
#Output:
#The output should contain the sum and average of the digits of all numbers that appear in the string. Note: Round the average value to two decimal places.
#Explanation:
#For example, if the given string is "I am 25 years and 10 months old", the digits of all numbers that appear in the string are 2, 5, 1, 0. Your code should print the sum of all digits(8) and the average of all digits (2.0) in the new line.
string = input()
num_list = []
for char in string:
    if char.isdigit():
        num_list.append(int(char))

summation = sum(num_list)
print(summation)
avg = summation/len(num_list)
print(round(avg,2))