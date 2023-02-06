#You are given a character as input. Check if the given input is a Lowercase Letter or Uppercase Letter or Digit or a Special Character
char = input()

lower = char.islower()
if lower:
    print("Lowercase Letter")
    
upper = char.isupper()
if upper:
    print("Uppercase Letter")

digit = char.isdigit()
if digit:
    print("Digit")

special = (not lower) and (not upper) and (not digit)
if special:
    print("Special Character")