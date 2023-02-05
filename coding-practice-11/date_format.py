#Write a program to convert the date from "dd-mm-yy" format to "dd/mm/yy" format.
date = input()
new_date_format = date.replace("-" , "/")

print(new_date_format)