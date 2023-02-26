#Unicode:
    #Computer internally stores characters as numbers. Every character has a unique unicode value.

character = input()
unicode_value = ord(character)
print(unicode_value)

#Character at Unicode:
unicode_value = int(input())
character = chr(unicode_value)
print(character)

#Unicode Ranges:
    # 48-57 ===> digits(0-9)
    # 65-90 ===> capital_letters(A-Z)
    # 97-122 ===> Small letters(a-z)
    # rest ===> special characters, other languages eg:!@#$%^&*?><:;\/., etc.


# COMPARING STRINGS: In python, string comparision is done character by character.
print("bad" > "BAD")
print("BAD" > "BAT")
print("98" <= "123")
print("98" <= "9876")


characters = ""
for i in range(123, 200):
    characters = characters + chr(i)
print(characters)