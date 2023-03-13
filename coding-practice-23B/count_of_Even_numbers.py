#A function is given in the prefilled code, that takes N space- separated integers as an argument.
#Write a program to return the count of even numbers among the given N space-separated numbers.
def get_even_numbers_count(numbers):
    # complete this function
    numbers_list = numbers.split(" ")
    length = len(numbers_list)
    
    count = 0
    for i in range(length):
        num = int(numbers_list[i])
        if num % 2 == 0:
            count += 1
    return count

numbers = input()
result = get_even_numbers_count(numbers) # call the get_even_numbers_count function
print(result)