#Write a program to compute the frequency of the characters other than space. Print the output in alphabetical order.
    #Note: Ignore the case of the characters.

def print_char_frequencies(line):
    line = line.lower()
    unique_chars = set(line)
    unique_chars.discard(' ')
    unique_chars = sorted(unique_chars)
    for char in unique_chars:
        msg = "{}: {}"
        print(msg.format(char, line.count(char)))
    

line = input()                      #Input:Tic Tac Toe
print_char_frequencies(line)        #Output:a: 1
                                    #       c: 2
                                    #       e: 1
                                    #       i: 1
                                    #       o: 1
                                    #       t: 3
