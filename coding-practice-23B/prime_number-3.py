#A function is given in the prefilled code that takes a number N as an argument.
#Write a program to check if the given number N is prime or not.
#Print Prime Number if the number is prime. Otherwise, print Not a Prime Number.
def is_prime(number):
    # complete this function
    factors = 0
    for i in range(1, number + 1):
        if number % i == 0:
            factors += 1
        else:
            pass
    if factors == 2:
        msg = "Prime Number"
    else:
        msg = "Not a Prime Number"
    
    return msg

number = int(input())
result =is_prime(number)  # call is_prime function
print(result)