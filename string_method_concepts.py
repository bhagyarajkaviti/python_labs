pin = "4567"
is_digit = pin.isdigit()
is_4_digit = (len(pin) == 4)
is_valid = is_digit and is_4_digit
print(is_valid)

mobile = "    984783438724   "
mobile = mobile.strip()
print(mobile)

name = "ravi765"
name = name.strip("765")
print(name)

name1 = "343333443ra345vi111"
name1 = name1.strip("3451")
print(name1) #output : ra345vi
#.strip("345") removes only the characters mentioned in the strip before starting of the string and after end of the string


#.replace(old_substring , new_substring)
message = "Edcation is a key factor. Right Edcation is important"
message = message.replace("Edcation", "Education")
print(message)

#startswith()
url = "https://google.com"
is_secure_url = url.startswith("https://")
print(is_secure_url)

#endswith()
gmail = "bhagyarajkaviti@gmail.com"
is_gmail = gmail.endswith("@gmail.com")
print(is_gmail)

#upper()
name2 = "bhagyaRaj"
print(name2.upper())

#lower()
name3 = "BHagyAraJ"
print(name3.lower())