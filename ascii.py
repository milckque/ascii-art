from PIL import Image
import numpy as np

ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ASCII_LEN = len(ASCII_CHARS) - 1
MAX_PIXEL_VALUE = 255

filepath = "pool1.jpg"
img = Image.open(filepath)
img_matrix = np.asarray(img)

intensity_matrix = []
for r in img_matrix:
    intensity_row = []
    for c in r:
        # luminosity with weighted avgs accounting for human perception
        intensity = 0.21 * c[0] + 0.72 * c[1] + 0.07 * c[2]
        intensity_row.append(intensity)
    intensity_matrix.append(intensity_row)

ascii_matrix = []
for r in intensity_matrix:
    ascii_row = []
    for c in r:
        # converting the luminosity of the pixel to a matching ascii character
        ascii_row.append(ASCII_CHARS[int( c / MAX_PIXEL_VALUE * ASCII_LEN)])
    ascii_matrix.append(ascii_row)

