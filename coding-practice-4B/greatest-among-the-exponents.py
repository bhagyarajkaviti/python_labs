#Write a program that reads two numbers A and B and finds the,
    # Result of A power B (AB)
    #Result of B power A (BA)
#Print the greatest among the results of A power B (A^B) and B power A (B^A).
A = int(input())
B = int(input())

result1 = A ** B
result2 = B ** A

if result1 > result2:
    print(result1)
else:
    print(result2)