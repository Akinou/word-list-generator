import random
import string

def generate_word_list(size):
    # Define a string containing all the letters of the alphabet
    letters = string.ascii_lowercase

    # Generate a list of random words
    word_list = []
    for i in range(size):
        word = ''.join(random.choice(letters) for i in range(random.randint(3, 10)))
        word_list.append(word)

    return word_list

# Prompt the user to choose the size of the word list
list_size = int(input("Enter the number of words to generate: "))

# Prompt the user to choose the size of each word
word_size = int(input("Enter the size of each word: "))

# Generate the word list
word_list = generate_word_list(list_size, word_size)

# Print the word list
print(word_list)
