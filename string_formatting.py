#String Formatting:
    #it increases readability of code and type conversions not required
    # Add placeholders{} where the string needs to be formatted
        # Syntax: msg.format(val_1, val_2, .....) ===> inserts values inside the strings placeholder{}

#Example 1:
name = input()              #Input:bhagyaraj
age = int(input())          #Input:26
msg = "Hi " + name + " you are " + str(age) + " years old"
print(msg)                  #Output:Hi bhagyaraj you are 26 years old
msg = "Hello {} you are {} years old" #Note: NUmber of placeholders{} cannot be more than the arguments passed to `format()` 
print(msg.format(name, age)) #Output:Hello bhagyaraj you are 26 years old  

#Example 2: Numbering placeholders
name = input()              #Input:ravi
age = int(input())          #Input:25
msg = "Hi {0} you are {1} years old"
print(msg.format(name, age))    #Output:Hi ravi you are 25 years old
msg = "Hello {1} you are {0} years old"
print(msg.format(name, age))    #Output:Hello 25 you are ravi years old

#Example 3: Naming placeholders
name = input()              #Input:raju
age = int(input())          #Input:21
msg = "Hi {arg_1} you are {arg_2} years old"
print(msg.format(arg_1=name, arg_2=age))    #Output:Hi raju you are 21 years old











