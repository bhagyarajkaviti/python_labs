#For this problem, the prefilled code will contain a dictionary. Write a program to remove a key.
#Input
#The input will be a single line containing a string, denoting the key to be removed.
#Output
#The output should be a single line containing the dictionary without the given key and its value.

students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

# Write your code here
n = int(input())

for i in range(n):
    key, value = input().split()
    students_dict[key] = value
    
print(students_dict)
    