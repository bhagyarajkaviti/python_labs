#For this problem, the prefilled code will contain a function. Write a program that the given function will check if the number N is divisible by 7.
def divisible_by_seven(arg_1):
    # Write your code here
    if arg_1 % 7 == 0:
        print(True)
    else:
        print(False)


n = int(input())
divisible_by_seven(n)
