# Default Argument Values   
def greet(arg_1="Hi", arg_2="Ram"):
    print(arg_1 + " " + arg_2)

greeting = input()      #Input :Good Morning
name = input()          #Input :Bhagyaraj      

greet()                         #Output :Hi Ram
greet(greeting)                 #Output :Good Morning Ram
greet(name)                     #Output :Bhagyaraj Ram
greet(greeting, name)           #Output :Good Morning Bhagyaraj
greet(arg_2=name)               #Output :Hi Bhagyaraj
greet("good evening", "Raj")    #Output :good evening Raj
greet("good night")             #Output :good night Ram
greet("Ravi")                   #Output :Ravi Ram

