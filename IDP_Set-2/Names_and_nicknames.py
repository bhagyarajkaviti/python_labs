#There are N people living in your village. You know the names and nicknames of all the people in the village.
#Write a program that reads the N people names and nicknames and checks whether any two people have the same name and nickname.
#Input
#The first line of the input contains an integer T representing the number of test cases. 
#The next lines of input contains,
#• The first line of the input contains an integer N representing the number of people living in the village.
#.The next N lines of input contains two space-separated strings representing the name and nickname of the person.

n = int(input())
names_matrix, nicknames_matrix = [],[]
for i in range(n):
    m = int(input())
    names_list = []
    nicknames_list = []
    for j in range(m):
        name, nickname = input().split()
        names_list.append(name)
        nicknames_list.append(nickname)
    names_matrix.append(names_list)
    nicknames_matrix.append(nicknames_list)
print(names_matrix)
print(nicknames_matrix)