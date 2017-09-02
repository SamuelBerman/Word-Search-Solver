from pytesseract import *
from PIL import Image
import os

img = Image.open(r'Test_Images\test2.png')
text = image_to_string(img)
text = '\n'.join([x for x in text.split("\n") if x.strip()!=''])

with open("Output.txt", "w") as text_file:
    print(text, file=text_file)
