#Write a function with name sum_of_squares_m_to_n that takes two integers (M and N) and sum the squares from M to N.
def sum_of_squares_m_to_n(m, n):
    # Complete this function
    output = 0
    for i in range(m, n + 1):
        output += i ** 2
    
    print(output)

m = int(input())
n = int(input())
# Call the sum_of_squares_m_to_n function
sum_of_squares_m_to_n(m, n)