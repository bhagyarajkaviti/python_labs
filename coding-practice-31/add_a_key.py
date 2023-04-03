#For this problem, the prefilled code will contain a dictionary. Write a program to add a key-value pair to the dictionary.
#Input
#The input will be a single line containing the strings, separated by space, denoting the key-value pair.
#Output
#The output should be a single line containing the dictionary with the added key-value pair.

students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

# Write your code here
input_data = input().split()
key, value = input_data
students_dict[key] = value
print(students_dict)