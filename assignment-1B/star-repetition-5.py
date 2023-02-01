string1 = input()
string2 = input()
l = len(string2)
result = l * "*" + string1[l:]
print(result)
#print(len(string2) * "*" + string1[len(string2):])