def greet(arg1, arg2):
    print(arg1 + " " + arg2)

greeting = input()
name = input()
#Keyword Arguments
greet(arg1=greeting, arg2=name)     #Output :Good Morning Bhagyaraj
greet(arg2=name, arg1=greeting)     #Output :Good Morning Bhagyaraj
#Positional Arguments
greet(greeting, name)               #Output :Good Morning Bhagyaraj
greet(name, greeting)               #Output :Bhagyaraj Good Morning
