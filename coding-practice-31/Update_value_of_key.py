#For this problem, the prefilled code will contain a dictionary. Write a program to update the value of a given key.
#Input
#The input will be a single line containing the strings, separated by space, denoting the key-value pair.
#Output
#The output should be a single line containing the dictionary with the updated value to the given key.

students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket",
    "Deepak": "Boxing"
}

# Write your code here
key,value = input().split()
students_dict[key] = value
print(students_dict)