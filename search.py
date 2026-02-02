import pytesseract
from PIL import Image
import os
import json

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

IMAGE_FOLDER = "images"
OUTPUT_FILE = "data.js"

pages_text = {}

for filename in sorted(os.listdir(IMAGE_FOLDER)):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        page = os.path.splitext(filename)[0]
        path = os.path.join(IMAGE_FOLDER, filename)

        print(f"OCR: {page}")
        text = pytesseract.image_to_string(Image.open(path))
        pages_text[page] = text.lower()

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("const data = ")
    json.dump(pages_text, f, indent=2)
    f.write(";")

print("\nDone! data.js created.")
