import cv2

# Read the image
image = cv2.imread("test.jpg")

# Check if it loaded correctly
if image is None:
    print("Could not read the image. Check the filename/path.")
else:
    print("Image loaded successfully!")
    print("Image size:", image.shape)  # prints height, width, color channels

    # Convert to grayscale (black and white) - a common first preprocessing step
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale version so you can see the result
    cv2.imwrite("test_gray.jpg", gray)
    print("Saved grayscale version as test_gray.jpg")