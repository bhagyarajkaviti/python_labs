def greet(word):
    msg = "Hello " + word
    return msg  #Returning value

name = input()
greeting = greet(word = name) # storing the value returned from the function into a variable
print(greeting)