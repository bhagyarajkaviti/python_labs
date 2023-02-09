#Write a program to print the numbers in the given N number of rows in the following square pattern.
#    1 2 3
#    4 5 6
#    7 8 9
n = int(input())

k = n
h = 1
for i in range(1, n + 1):
    output = ""
    for j in range(h , k + 1):
        output = output + str(j) + " "
    k = k + n
    h = h + n
    print(output)
    

# Another solutuion

#n = int(input())

#number = 1
#for i in range(n):
#    pattern = ""
#    for j in range(n):
#        pattern = pattern + (str(number) + " ")
#        number = number + 1
#    print (pattern)