"""
Author: Travis Tran
Email: tran@travis.guru
Github: travistran1989
Description: Generating a comparison image of two fonts by overlap same code characters.

Copyright 2023 Pitagon., JSC. All rights reserved.
"""
# This script is meant to be run from the root level
# of your font's git repository. For example, from a Unix terminal:
# $ git clone my-font
# $ cd my-font
# $ python3 documentation/image2.py

# Import modules from external python packages: https://pypi.org/
import math
import string

from fontTools.ttLib import TTFont
from PIL import ImageFont, ImageDraw, Image

# Set the size of the font.
FONT_SIZE = 500
FONT_PATH_1 = "../sources/release/v1.0.1/ttf/PitagonSans-Regular.ttf"
FONT_PATH_2 = "../fonts/ttf/PitagonSans-Regular.ttf"
OUTPUT = "documentation/image2.png"
NUM_CHAR_LINE = 20
LINE_GAP = 50

def get_unicode_chars(font_path):
    # Load the font using the fontTools library.
    font = TTFont(font_path)

    # Get a list of all the character names in the font.
    glyph_names = font.getGlyphNames()

    # Get a list of all the Unicode characters in the font.
    # The getBestCmap() function returns a dictionary that maps character codes to glyph names.
    cmap = font.getBestCmap()
    unicode_chars = [chr(code) for code in cmap.keys()]

    return unicode_chars

def get_max_char_size(font, chars):
    max_width = 0
    max_height = 0

    for char in chars:
        bbox = font.getbbox(char)
        if bbox is not None:
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            max_width = max(max_width, width)
            max_height = max(max_height, height)

    return max_width, max_height

def generate_comparison_image(font_path1, font_path2, output_path, text=None):

    # Load the two fonts
    font1 = ImageFont.truetype(font_path1, FONT_SIZE)
    font2 = ImageFont.truetype(font_path2, FONT_SIZE)

    # Decide which characters to use.
    if text is None:
        # # Use all printable ASCII characters.
        # common_chars = string.printable
        # # Use all characters that exist in both fonts.
        # common_chars = set(c for c in font1.get_chars() if c in font2.get_chars())
        chars1 = set(get_unicode_chars(font_path1))
        chars2 = set(get_unicode_chars(font_path2))
        # Only compare characters that are present in both fonts.
        common_chars = chars1 & chars2
    else:
        # Use only the characters provided by the user.
        common_chars = text

    # Calculate the size of the image based on the number of characters and the size of the characters.
    num_chars = len(common_chars)
    max_width1, max_height1 = get_max_char_size(font1, common_chars)
    max_width2, max_height2 = get_max_char_size(font2, common_chars)
    char_width = max(max_width1, max_width2)
    char_height = max(max_height1, max_height2)
    image_width = NUM_CHAR_LINE * char_width
    num_lines = math.ceil(num_chars / NUM_CHAR_LINE)
    image_height = num_lines * (char_height + LINE_GAP) + char_height

    # Create two new images, one for each text layer.
    layer1 = Image.new('RGBA', (image_width, image_height), (0, 0, 0, 0))  # Use RGBA for transparency.
    layer2 = Image.new('RGBA', (image_width, image_height), (0, 0, 0, 0))

    draw1 = ImageDraw.Draw(layer1)
    draw2 = ImageDraw.Draw(layer2)

    # Draw each character at the correct position.
    for i, char in enumerate(common_chars):
        x = (i % NUM_CHAR_LINE) * char_width
        y = (i // NUM_CHAR_LINE) * (char_height + LINE_GAP)
        draw1.text((x, y), char, fill=(255, 0, 0, 128), font=font1)
        draw2.text((x, y), char, fill=(0, 255, 255, 128), font=font2)

    # Blend the images together and save the result.
    output = Image.alpha_composite(layer1, layer2)
    output.save(output_path)

# Build and save the image
if __name__ == "__main__":
    generate_comparison_image(FONT_PATH_1, FONT_PATH_2, OUTPUT, "ABCDEFGHIJKLMNOPQRSTUV")
    print("Characters Comparison: Done")
