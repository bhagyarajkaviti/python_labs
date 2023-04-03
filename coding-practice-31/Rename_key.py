#For this problem, the prefilled code will contain a dictionary. Write a program to rename a key in the dictionary with the given name.
#Input
#The first line of input will contain a string, denoting the existing key in the dictionary.
#The second line of input will contain a string, denoting the new key to be renamed.
#Output
#The output should be a single line containing the list of tuples with dictionary items, where the key is updated without changing the order of the key-value pairs.

fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15,
    "oranges": 200,
    "watermelons": 50
}

# Write your code here
key = input() 
new_key = input() 

fruit_items = list(fruits.items()) 
fruit_items_copy = fruit_items.copy()
fruits_count = len (fruit_items)

for i in range(fruits_count):
    if fruit_items[i][0] == key:
        updated_tuple = (new_key, fruit_items[i][1])
        fruit_items_copy[i] = updated_tuple
print (fruit_items_copy)





# another solution
    
    
#old_key = input()
#new_key = input()

#keys_list = list(fruits.keys())
#index = keys_list.index(old_key)
#keys_list[index] = new_key

#value_list = list(fruits.values())
#output_list = []
#for i in range(len(keys_list)):
#    key, value = keys_list[i], value_list[i]
#    item = key, value
#    output_list.append(item)
#print(output_list)


