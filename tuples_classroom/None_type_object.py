# `None` is an object which is a datatype of its own (NoneType). `None` is used to define no value (or) Nothing.

#Example 1:
var = None
print(var)          #Output:None
print(type(var))    #Output:<class 'NoneType'>

#Example 2:
def increment(a):
    a += 1

a = int(input())        #input:9
result = increment(a)
print(result)           #Output:None
