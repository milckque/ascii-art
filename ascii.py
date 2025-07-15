from PIL import Image
import numpy as np

ASCII_CHARS = " `^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ASCII_LEN = len(ASCII_CHARS) - 1
MAX_PIXEL_VALUE = 255

filepath = "kirby.png"

img = Image.open(filepath)
width, height = img.size
bigger = max(width, height)
img = img.resize((int(width/bigger * 100), int(height/bigger * 100)))
img_matrix = np.asarray(img)

intensity_matrix = []
for r in img_matrix:
    intensity_row = []
    for c in r:
        # luminosity with weighted avgs accounting for human perception
        intensity = 0.21 * c[0] + 0.72 * c[1] + 0.07 * c[2]
        intensity_row.append(intensity)
    intensity_matrix.append(intensity_row)

normalised_intensity_matrix = []
max_pixel = max(map(max, intensity_matrix))
min_pixel = min(map(min, intensity_matrix))
for r in intensity_matrix:
    normalised_intensity_row = []
    for c in r:
        normalised_intensity_row.append(MAX_PIXEL_VALUE * (c - min_pixel) / float(max_pixel - min_pixel))
    normalised_intensity_matrix.append(normalised_intensity_row)

ascii_matrix = []
for r in normalised_intensity_matrix:
    ascii_row = []
    for c in r:
        # converting the luminosity of the pixel to a matching ascii character
        ascii_row.append(ASCII_CHARS[int( c / MAX_PIXEL_VALUE * ASCII_LEN)])
    ascii_matrix.append(ascii_row)

for r in ascii_matrix:
    row = [c+c+c for c in r]
    print("".join(row))