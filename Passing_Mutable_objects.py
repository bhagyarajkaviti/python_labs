#EXample 1:
def add_item(list_x):
    list_x += [3] #list_a and list_x is referring the same object 
    
list_a = [1,2]
print(list_a)   #Output:[1, 2]
add_item(list_a)
print(list_a)   #Output: [1, 2, 3]


#EXample 2:
def add_item(list_x):
    list_x = list_x + [3] #list_a is referring different object and list_x is referring different object.
    
list_a = [1,2]
print(list_a)   #Output:[1, 2]
add_item(list_a)
print(list_a)   #Output: [1, 2]


#EXample 3: Default Arguments
def add_item(list_x = []):
    list_x += [3] 
    print(list_x)    

add_item()          #Output:[3]
add_item([1, 2])    #Output:[1, 2, 3]
add_item()          #Output:[3, 3]
add_item()          #Output:[3, 3, 3]
add_item()          #Output:[3, 3, 3, 3]





