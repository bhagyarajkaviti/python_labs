#You are given a sentence. Write a program to remove all the vowels in the given sentence.
#Note: Sentence has both lowercase and uppercase letters.
string = input()

string = string.replace("a", "")
string = string.replace("A", "")
string = string.replace("E", "")
string = string.replace("e", "")
string = string.replace("I", "")
string = string.replace("i", "")
string = string.replace("O", "")
string = string.replace("o", "")
string = string.replace("U", "")
string = string.replace("u", "")

print(string)


# Alternate and simple solution for this problem

#n = input()
#vowels = ('a','e','i','o','u')


#for i in n:
#    if i.lower() in vowels:
#        n = n.replace(i,"")
#print(n)
