string_a = "Python is a programming language"
list_a = string_a.split('a')
print(list_a)           #output : ['Python is ', ' progr', 'mming l', 'ngu', 'ge']

#Syntax :string.join(sequence)
string_2 = "a".join(list_a) 
print(string_2)         #output : Python is a programming language           