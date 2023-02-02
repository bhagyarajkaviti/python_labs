#Write a program that reads a string S and checks if all the given conditions are satisfied.
    #The first three characters of S is NXT.
    #The remaining characters of S contain a Number. Number is divisible by 2 or 7.
#Print Special String if all the given conditions are satisfied. Otherwise, print Not a Special String.
string = input()

condition1 = string[:3] == "NXT"
condition2 = (int(string[3:]) % 2 == 0) or (int(string[3:]) % 7 == 0)

if condition1 and condition2:
    print("Special String")
else:
    print("Not a Special String")