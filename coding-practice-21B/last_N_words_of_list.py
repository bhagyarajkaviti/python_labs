#Given space-separated words S and a number N. Write a program that creates a list using space-separated words and prints the last N words of the list in reverse order.
string = input()
n = int(input())

string_list = string.split()
reverse_string = (string_list[::-1])

output_string = reverse_string[:n]
print(output_string)