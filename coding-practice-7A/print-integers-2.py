#Given two integer numbers M and N, write a program to print the integers from M to N.
M = int(input())
N = int(input())

count = M

while count >= M and count <= N:
    print(count)
    count = count + 1


#while M <= N:
    #print(M)
    #M = M + 1