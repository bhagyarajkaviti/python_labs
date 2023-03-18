#Write a function with the name fizz_buzz that takes a number as an argument.
#- If the number is divisible by 3, it should return "Fizz".
#- If it is divisible by 5, it should return "Buzz".
#- If it is divisible by both 3 and 5, it should return "FizzBuzz".
#- Otherwise, it should return the same number.
def fizz_buzz(number):
    if number < 0:
        number = -number
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    
    else:
        return number

number = int(input())
result = fizz_buzz(number)
print(result)