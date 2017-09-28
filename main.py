from pytesseract import *
from PIL import Image
import os


# load image and convert to string 
img = Image.open(os.path.join(r'Test_Images', r'test2.png'))
text = image_to_string(img)


# create dict with key being (x,y) tuple and value being the letter
def string_to_array(string):
    string = '\n'.join([x for x in string.split("\n") if x.strip()!=''])
    letter_positions = {}

    for (y, row) in enumerate(string.split('\n')):
        for (x, letter) in enumerate(row):
             letter_positions[x,y] = letter
             
    return letter_positions


def find_word(word, array):
    letters = list(word)
    possible_answer = []
    first_letters = []
    iteration = 0

    for letter in array:
        if array[letter] == letters[0]:
            first_letters.append(letter)

    
    def recurse(letter):
        global letters
        global possible_answer
        global array
        global word
        global iteration
        
        # check right
        for x in range(1, (len(word) + 1)):
            if array.get((letter[0] + x, letter[1]), None) == letters[x-1]:
                possible_answer.append(letter)
                possible_answer.append((letter[0]+x, letter[1]))

    
    for letter in first_letters:
        recurse(letter)
        
    print(possible_answer)
    

word_array = string_to_array(text)
find_word("MELT", word_array)
