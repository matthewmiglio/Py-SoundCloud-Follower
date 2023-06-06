import pytesseract
from PIL import Image


tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def read_image_text(
    image,
    
    segmentation_mode="single_line",
    engine_mode="default",
):
    # Set the path to the Tesseract executable
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    # Open the image file
    # image = Image.open(image_path)

    # Convert the image to grayscale
    image = image.convert("L")

    # Set the configuration options for Tesseract
    config = ""

    # handle text segmentation configuation
    if segmentation_mode == "no_segmentation":
        config += " --psm 0"  # analyzes the image to determine the orientation of the text (e.g., upright or rotated) and the script being used (e.g., Latin, Cyrillic, etc.).
    elif segmentation_mode == "paragraph":
        config += " --psm 3"  # assumes a single block of text and tries to segment it into paragraphs, lines, and words
    elif segmentation_mode == "single_column":
        config += " --psm 4"  # Treat the image as a single column of text
    elif segmentation_mode == "single_line":
        config += " --psm 7"  # Treat the image as a single line of text

    # handle engine mode configuation
    if engine_mode == "original":
        config += " --oem 0"
    elif engine_mode == "neural_net_LSTM":
        config += " --oem 1"
    elif engine_mode == "tesseract_LSTM":
        config += " --oem 2"
    elif engine_mode == "default":
        config += " --oem 3"

    # print(f"The config im about to use: [{config}]")

    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(image, config=config)

    # Return the extracted text
    return text.strip()
