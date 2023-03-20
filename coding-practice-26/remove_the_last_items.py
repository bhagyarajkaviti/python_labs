#For this problem, the prefilled code will contain a list. Write a program to remove the last N items in the list.
programming_languages = ['Python', 'C', 'Java', 'Ruby', 'C++', 'CSS', 'HTML', 'Bash', 'Perl', 'R', 'Swift', 'SQL', 'PHP', 'JavaScript']

n = int(input())
for i in range(n):
    programming_languages.remove(programming_languages[-1])
print(programming_languages)