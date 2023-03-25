#For this problem, the prefilled code will contain a set. Write a program to add an word W to the set.
#The input will be a single line containing a string (W).
#The output should be a single line containing the list in ascending order.

set_a = {"pencil"}

word = input()

set_a.update([word]) #here the string is converted into as a list item and then this item updated to set_a

list_a = list(set_a)
list_a.sort()
print(list_a)
