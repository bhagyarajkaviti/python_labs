#Write a program that prints the individual characters of the given word separated with hyphens ("-").
a = input()
len_of_a = len(a)
b = a[0]
for i in range(1, len_of_a):
    b = b + "-" + a[i]
print(b)
