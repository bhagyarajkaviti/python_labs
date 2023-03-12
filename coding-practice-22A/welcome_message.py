#For this problem, the prefilled code will contain a function. Write a program to concatenate the message "Welcome" followed by the given name.
def say_wishes(arg_1):
    # Write your code here
    message = "Welcome " + arg_1
    print(message)
    
name = input()
say_wishes(name)
