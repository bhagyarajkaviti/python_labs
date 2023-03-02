#example 1:
list_a = [1, 2, 3]  #list_a is reffering to this new object[1, 2, 3]
list_b = [1, 2, 3]  #list_b is reffering to this new object[1, 2, 3]
print(id(list_a))   #output:2212301656896
print(id(list_b))   #output:2212303239104

#example 2:
list_a = [1, 2, 3]
list_b = list_a
print(id(list_a))   #output:2212303332032
print(id(list_b))   #output:2212303332032

#example 3:
list_a = [1, 2, 3, 5]
list_b = list_a
list_b[3] = 4
print("list a : " + str(list_a))    #Output:list a : [1, 2, 3, 4]
print("list b : " + str(list_b))    #Output:list b : [1, 2, 3, 4]

#example 3A:
list_a = [1, 2, 3, 5]
list_b = list_a
list_a[0] = 4
print("list a : " + str(list_a))    #Output:list a : [4, 2, 3, 5]
print("list b : " + str(list_b))    #Output:list b : [4, 2, 3, 5]

#example 4:
list_a = [1, 2]
list_b = list_a
list_a = list_a + [6, 7]
print("list a : " + str(list_a))    #Output:list a : [1, 2, 6, 7]
print("list b : " + str(list_b))    #Output:list b : [1, 2]

#example 4A:
list_a = [1, 2]
list_b = list_a
list_a += [6, 7] # Compound assignment operator updates the object inplace which means updating the same object refered by two variables (list_a and list_b)
print("list a : " + str(list_a))    #Output:list a : [1, 2, 6, 7]
print("list b : " + str(list_b))    #Output:list b : [1, 2, 6, 7]

#example 5:
list_a = [1, 2]
list_b = [3, list_a]
list_a[1] = 4
print("list a : " + str(list_a))    #Output:list a : [1, 4]
print("list b : " + str(list_b))    #Output:list b : [3, [1, 4]]

#example 6:
a = 2
list_a = [1, a]
print(list_a)       #Output:[1, 2]
a = 3
print(list_a)       #Output:[1, 2]
