from pytesseract import *
from PIL import Image
import os


# create list of lists from string
def string_to_array(string):
    string = string.upper()
    string = '\n'.join([x for x in string.split("\n") if x.strip() != ''])
    array = []

    for line in string.split('\n'):
        array.append(list(line))

    return array


def check_in_direction(array, word, x, y, dx, dy, letters=None):
    letters = letters or []

    if len(word) <= 0:
        return letters

    if not 0 <= y < len(array):
        return None

    if not 0 <= x < len(array[y]):
        return None

    if array[y][x] != word[0]:
        return None

    letters.append((x, y))

    word = word[1:]

    x += dx
    y += dy

    return check_in_direction(array, word, x, y, dx, dy, letters=letters)


def find_word(word, array):
    word = word.upper()

    for y, line in enumerate(array):
        for x, char in enumerate(line):
            # check for the word in all directions
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if (dx, dy) == (0, 0):
                        continue

                    letters = check_in_direction(array, word, x, y, dx, dy)

                    if letters != None:
                        return letters
    return None


def output(letters, array):
    for y, line in enumerate(array):
        for x, char in enumerate(line):
            for letter in letters:
                if (x, y) == letter:
                    array[y][x] = r"<b>{}</b>".format(char)

    with open('output.html', 'w+') as f:
        f.write(r'<font size="10"><pre>')
        for line in array:
            f.write(''.join(line) + r"<br />")
        f.write(r'</pre></font>')


# load image and convert to array
print("Starting...")

img = Image.open(os.path.join(r'Test_Images', r'test2.png'))
text = image_to_string(img)
word_array = string_to_array(text)

print("Successfully converted to array!")

found_words = []

for x in range(sum(1 for line in open('words.txt'))):
    letters = find_word(open('words.txt').readlines()[x].strip(), word_array)
    if letters != None:
        found_words.append(letters)

print(len(found_words), "out of", sum(1 for line in open('words.txt')), "words match!")

if len(found_words) == 0:
    print("No Matching Words!")
    output([], word_array)
    
else:
    for x in range(len(found_words)):
        output(found_words[x], word_array)
    print("Output complete!")

print("Done!")
