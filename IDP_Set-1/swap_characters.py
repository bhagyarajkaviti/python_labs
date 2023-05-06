#Arjun has two strings S and T. In order to equal them, he can select any two adjacent characters in S and swap them only once.
#Write a program that reads two strings and checks if Arjun can make the given two strings equal or not.
#Input
#The first line of input contains a string representing S. The second line of input contains a string representing T.
#Output
#The output should be a single line containing a string. Yes should be printed if the given two strings are equal after swapping any two adjacent characters in S, otherwise No should be printed.


string1 = input()
string2 = input()

first_list,second_list = list(string1),list(string2)
for i in range(len(first_list)-1):
    if first_list[i] != second_list[i]:
        pick = first_list[i]
        first_list[i] = first_list[i+1]
        first_list[i+1]= pick
        break
    
if first_list == second_list:
    print("Yes")
else:
    print("No")








