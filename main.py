from pytesseract import *
from PIL import Image
import os

word = "hippo"

# load image and convert to string
img = Image.open(r'Test_Images\test2.png')
text = image_to_string(img)

def string_to_array(string):
    string = '\n'.join([x for x in string.split("\n") if x.strip()!=''])
    array = []
    lines = string.split('\n')
    
    for line in lines:
        array.append(list(line))

    return array

word_array = string_to_array(text)

print(word_array)
