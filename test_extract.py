import pytesseract
import cv2
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = cv2.imread("test_gray.jpg")
text = pytesseract.image_to_string(image)

print("----- RAW OCR TEXT -----")
print(text)

# Example pattern: find anything that looks like a course code (e.g. CSA4028, HUM1002)
course_codes = re.findall(r"[A-Z]{2,4}\d{3,4}", text)

# Example pattern: find names (all-caps words, 2+ letters, appearing on their own)
# This is a simple approach - real name detection is harder, this is a starting point
names = re.findall(r"\b[A-Z]{3,}\b", text)

print("\n----- EXTRACTED COURSE CODES -----")
print(course_codes)

print("\n----- POSSIBLE NAMES -----")
print(names)