import pytesseract
import cv2

# Tell Python where Tesseract is installed
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read the grayscale image you already created
image = cv2.imread("test_gray.jpg")

# Extract text from it
text = pytesseract.image_to_string(image)

print("Extracted text:")
print(text)