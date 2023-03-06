#example 1:

nums = "1 2 3 4"
num_list = nums.split()     # if no seperator is specified, default seperator is white space.
print(num_list)         #output : ['1', '2', '3', '4']

#example 2:
nums = "1    2 3   4"
num_list = nums.split()    #multiple whitespaces are considered as single when splitting.
print(num_list)         #output : ['1', '2', '3', '4']

#example 3:

nums = "1\n2\t3 4"
num_list = nums.split()     #New line (\n) and tab space (\t) are also whitespace.
print(num_list)         #output : ['1', '2', '3', '4']

#example 4:
nums = "1,2,3,,4,,"
num_list = nums.split(',')
print(num_list)             #output : ['1', '2', '3', '', '4', '', '']

#example 5:
string_a = "Python is a programming language"
list_a = string_a.split('a')
print(list_a)               #output : ['Python is ', ' progr', 'mming l', 'ngu', 'ge']
