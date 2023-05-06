#Aryan has two strings S and T containing lowercase alphabets. His student Ram has been asked to encode the string in the following manner.
#Ram should think a positive number K that may transform S into T by shifting each character of S to the right of K positions.
#For example,
#• If K = 2 then a is shifted to the right of 2 positions, it will become c.
#• If K = 3 then x is shifted to the right of 3 positions, it will become a.
#Your task is to help Aryan determine whether Ram can transform S into T after encoding.
#Write a program that reads the two strings S and T and checks if Ram can transform S into T by encoding the string.


def check_string_transformation(s, t):
    expected_difference = (ord(t[0]) - ord(s[0])) % 26
    can_transform_string = "Yes"
    for i in range(len(s)):
        current_difference = (ord(t[i]) - ord(s[i])) % 26
        if (current_difference != expected_difference):
            can_transform_string = "No"
    return can_transform_string
    
def main():
    s, t = input(), input()
    can_transform_string = check_string_transformation(s, t)
    print(can_transform_string)
    
main()