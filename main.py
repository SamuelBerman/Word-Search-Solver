from pytesseract import *
from PIL import Image
import os


# load image and convert to string
img = Image.open(os.path.join(r'Test_Images', r'test2.png'))
text = image_to_string(img)


# create list of lists from string
def string_to_array(string):
    string = '\n'.join([x for x in string.split("\n") if x.strip()!=''])
    array = []

    for line in string.split('\n'):
        array.append(list(line))

    return array


def find_word(word, array):
    chars = list(word)

    for y, line in enumerate(array):
        for x, char in enumerate(line):
            if char == chars[0]:
                print(x, y)
                # check for the word in all directions


word_array = string_to_array(text)
find_word("MELT", word_array)
