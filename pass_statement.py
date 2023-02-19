#'pass' statement is used as a syntactic place holder
age = int(input())
output = ""

if age >= 20:
    output = "your age is " + str(age) + " you are an adult now"
elif age > 12:
    pass
else:
    output = "your age is " + str(age)+ " you are a child now"
print(output)