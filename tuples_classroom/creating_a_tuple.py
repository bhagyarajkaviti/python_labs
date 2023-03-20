# Tuple holds an ordered sequence of items.
# `Tuple` is `Immutable object` where as `list` is a `Mutable object`
# `Tuple` is created by enclosing elements with in (round) brackets. Each item is seperated by a comma(,)

#Example 1:
a = 2
tuple_a = (5, "six", a, 8.2)
print(type(tuple_a))        #Output:<class 'tuple'>
print(tuple_a)              #Output:(5, 'six', 2, 8.2)

#Example 2:
a = ()
b = (5)
c = (1,2,3)
print(type(a))  #Output:<class 'tuple'>
print(type(b))  #Output:<class 'int'>
print(type(c))  #Output:<class 'tuple'>

#Example 3: incase of we create a tuple with single item, then we have to give a comma after the item.
a = (1,)
print(type(a))  #Output:<class 'tuple'>
print(a)        #Output:(1,)

# Accessing tuple elements
#Example 1:
a = 2
tuple_a = (5, "six", a , 8.2)
print(tuple_a[1])   #Output:six