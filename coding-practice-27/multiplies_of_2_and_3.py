#Given an integer N. Write a program to create two sets with N multiples of 2 and 3 and print the following
#1. All the multiples of 2 but not the multiplies of 3
#2. Uncommon multiples of 2 and 3
n = int(input())

multiples_of_2 = []
multiples_of_3 = []
for i in range(1, n+1):
    multiples_of_2 += [2*i]
    multiples_of_3 += [3*i]
multiples_of_2_set = set(multiples_of_2)
multiples_of_3_set = set(multiples_of_3)

output_1 = multiples_of_2_set.difference(multiples_of_3_set) #Set Difference
print(sorted(output_1)) #All the multiples of 2 but not the multiplies of 3

output_2 = multiples_of_2_set.symmetric_difference(multiples_of_3_set) # Set Symmetric Difference
print(sorted(output_2)) # All the Uncommon multiples of 2 and 3