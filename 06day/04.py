from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open(r'Z:\2.jpg'))
print(text)