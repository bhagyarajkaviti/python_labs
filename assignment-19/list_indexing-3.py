#Given N numbers, and an index, write a program to store the numbers in a list and print the number at the given index.
# For this problem, each input will contain T test cases. Each test case will give an index Ki as input, which should be considered to print the number.
n =int(input())
no_of_test_cases = int(input())

numbers_list = []
for i in range(n):
    numbers = int(input())
    numbers_list += [numbers]
for j in range(no_of_test_cases):
    test_case = int(input())
    print(numbers_list[test_case])
    
#Another solution for the same question
#a=int(input())
#t=int(input())
#number=[int(input())for i in range(a)]

#for i in range(t):
#    print(number[int(input())])