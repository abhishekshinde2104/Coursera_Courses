from PIL import Image

image = Image.open("text.png")
display(image)

import pytesseract
text = pytesseract.image_to_string(image)
print(text)
