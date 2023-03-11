#Given space-separated numbers.
#Write a program that prints a string by joining the given space- separated numbers with the comma(, ).
numbers_list = input().split()
required_numbers_pattern = ",".join(numbers_list)
print(required_numbers_pattern)