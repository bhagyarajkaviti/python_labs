#Write a function with the name validate_atm_pin_code that takes a word as an argument.
#ATM PIN is considered valid only if the given word contains
#- Exactly 4 or 6 characters
#- All the characters should be digits
def validate_atm_pin_code(pin):
    if pin.isdigit() and (len(pin) == 4 or len(pin) == 6):
        return "Valid PIN Code"
    else:
        return "Invalid PIN Code"

pin = input()
result = validate_atm_pin_code(pin)
print(result)
