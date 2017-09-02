from PIL import Image
from pytesseract import *

image_file = r'Test_Images\test.png'
im = Image.open(image_file)
text = image_to_string(im)
text = image_file_to_string(image_file)
text = image_file_to_string(image_file, graceful_errors=True)
print("=====output=======\n")
print(text)
