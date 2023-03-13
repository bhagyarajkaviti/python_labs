#A function is given in the prefilled code that takes a number N as an argument.
#Write a program that returns the factors of the given number N separated by a space as shown in the sample output.
def factors_of_n(number):
    # complete this function    
    output = ""
    for i in range(1,number + 1):
        if number % i == 0:
            output += str(i) + " "
            
    return output

number = int(input())
result = factors_of_n(number) # call the factors_of_n function
print(result)