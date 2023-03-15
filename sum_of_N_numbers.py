def sum_of_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_numbers(n - 1)
    
num = int(input())      #input:4
result = sum_of_numbers(num)
print(result)           #output:10