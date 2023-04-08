#Write a program that reads a sentence and prints the sum and average of the numbers that appear in the sentence, ignoring all other characters.
#Input
#The input will be a single line containing a string representing a sentence.
#Output
#The first line of output should be an integer which is the sum of the numbers in the given sentence.
#The second line of output should be a float that is the average of the numbers in the given sentence.
#Explanation
#For example, if the given sentence is I am 25 years and 10 months old.
#The numbers in the sentence are 25 and 10.
#The sum of the numbers is 35. (25 + 10 = 35)
#The average of the numbers is 17.5. ( 35/2 = 17.5)

sentence=input()
new=[]
num=""
for i in sentence:
    if i.isdigit():
        num=num+i
    else:
        num=num+" "
new=num.split()
total_seq=list((new))
#print(total_seq)
length = (len(total_seq))
sum_1 = 0
for i in total_seq :
    integer = int(i)
    sum_1+=((integer))
    
Add=(sum_1)
Avg = sum_1/length

print(Add)
print(round(Avg,2))

