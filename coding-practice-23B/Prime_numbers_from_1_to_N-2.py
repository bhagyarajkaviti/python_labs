#A function is given in the prefilled code that takes a number N as an argument.
#Write a program that returns all the prime numbers from 1 to N separated by a space.
def is_prime(n):
    # complete this function
    output = ""
    for i in range(1, n + 1):
        factors = 0
        for j in range(1, i + 1):
            if i % j == 0:
                factors += 1
                
        if factors == 2:
            output += str(i) + " "
        else:
            pass
        
    return output

n = int(input())

# call the is_prime function
print(is_prime(n))