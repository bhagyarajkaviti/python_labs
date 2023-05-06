#A group of people are playing a game. Each person stands in a line and holds a card with a number on it.
#You will be given a random number S and your task is to find
#• The updated group of people after removing the S number of people from the left side of the group.
#• The updated group of people after removing the S number of people from the right side of the group.
#Write a program that reads the card numbers and a random number S and prints the updated group of people in two lines after removing the S number of people from the left and right sides of the group.
#Input
#The first line of input contains comma-separated integers representing the card numbers. The second line of input contains an integer representing the random number S.


num_list = list(map(int, input().split(",")))
s = int(input())

rightside_list = num_list[s:]
print(*rightside_list)

leftside_list = num_list[:-s]
print(*leftside_list)