#Given an integer N, write a program to print the given N inputs in the reverse order.
n = int(input())

reversed_list = ""
for i in range(n):
    item = input()
    reversed_list = item + "\n" + reversed_list
print(reversed_list)