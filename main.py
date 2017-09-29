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


def check_in_direction(array, word, x, y, dx, dy):
    if len(word) <= 0:
        return True

    if not 0 <= y < len(array):
        return False

    if not 0 <= x < len(array[y]):
        return False

    if array[y][x] != word[0]:
        return False

    word = word[1:]

    x += dx
    y += dy

    return check_in_direction(array, word, x, y, dx, dy)


def find_word(word, array):
    chars = list(word)

    for y, line in enumerate(array):
        for x, char in enumerate(line):
            # check for the word in all directions
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if (dx, dy) == (0, 0):
                        continue

                    if check_in_direction(array, word, x, y, dx, dy):
                        return True
    return False


word_array = string_to_array(text)
find_word("MELT", word_array)
