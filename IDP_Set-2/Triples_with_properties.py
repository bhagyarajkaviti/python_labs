#Shikhar has two integers S and T. He wants to count all possible triplets of non-negative integers (a, b, c) which satisfy the below conditions:
#a + b + c <= S and a x bx c <= T
#Your task is to help Shikhar by finding the count of such triplets.
#Write a program that reads the two space-separated numbers S and T, and prints the count of triplets of non-negative integers (a, b, c) satisfying the above conditions.
#Note
#A group of three, considered as a unit is known as triplet.

s, t = map(int, input().split())
triplets = 0
for a in range(s+1):
    for b in range(s+1):
        for c in range(s+1):
            if (a + b + c) <= s and (a * b * c) <= t:
                triplets += 1
print(triplets)