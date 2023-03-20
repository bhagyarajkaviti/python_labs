# Operations on tuples
tuple_a = (2, 4.5, "abc", 10)

print(len(tuple_a))         #Output:4
for item in tuple_a:
    print(item)             #Output:2
                            #       4.5
                            #       abc
                            #       10       
print(tuple_a[1:3])         #Output:(4.5, 'abc')
print(tuple_a[0:3:2])       #Output:(2, 'abc')