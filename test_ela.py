from PIL import Image, ImageChops, ImageEnhance
import os

def perform_ela(image_path, quality=90):
    # Step 1: Open the original image
    original = Image.open(image_path).convert("RGB")

    # Step 2: Save it again as a JPEG at a known quality level
    # This is the "resave" that edited regions will react differently to
    temp_path = "temp_resaved.jpg"
    original.save(temp_path, "JPEG", quality=quality)

    # Step 3: Re-open the resaved version
    resaved = Image.open(temp_path)

    # Step 4: Find the difference between original and resaved
    diff = ImageChops.difference(original, resaved)

    # Step 5: Boost the differences so they're visible to the human eye
    # (real differences are usually very small pixel values, so we amplify them)
    extrema = diff.getextrema()  # gets the min/max difference values per channel
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1  # avoid dividing by zero
    scale = 255.0 / max_diff

    ela_image = ImageEnhance.Brightness(diff).enhance(scale)

    # Step 6: Save the result so you can look at it
    ela_image.save("ela_result.jpg")

    # Clean up the temporary file
    os.remove(temp_path)

    print("ELA complete. Check ela_result.jpg")
    print("Max difference found:", max_diff, "(higher can mean more editing/artifacts)")

# Run it on your test image
perform_ela("test_edited.jpg")