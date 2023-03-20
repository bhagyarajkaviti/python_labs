#Example:
set_a = {1, 2, 3, 9, 7, 1, 2}
print(set_a)            #Output:{1, 2, 3, 7, 9}
print(len(set_a))       #Output:5

for item in set_a:
    print(item)         #Output:1
                        #       2
                        #       3
                        #       7
                        #       9

is_part = 9 in set_a
print(is_part)          #Output:True
is_part = 10 not in set_a
print(is_part)          #Output:True

set_a.clear()
print(set_a)            #Output:set()
 