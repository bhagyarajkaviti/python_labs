#Write a function with the name count_the_vowels that takes a word as an argument and count the number of vowels in the given word. The letters (a, e, i, o, u) are considered as vowels.
def count_the_vowels(word):
    # Complete this function
    word = word.lower()
    
    count = 0
    for char in word:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            count += 1
    
    return count


word = input()
# Call the count_the_vowels function
print(count_the_vowels(word))