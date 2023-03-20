#Tuple packing: Values seperated by commas will be packed into a tuple.
#Note:() brackets are optional while creating tuples

#Example 1:
a = 1, 2, 3
print(type(a))      #Output:<class 'tuple'>
print(a)            #Output:(1, 2, 3)

#Example 2:  Packing Vs Unpacking
#Packing
a = 1,
print(type(a))     #Output:<class 'tuple'>
print(a)           #Output:(1,)
#Unpacking
a, = 1,
print(type(a))     #Output:<class 'int'>
print(a)           #Output:1  





