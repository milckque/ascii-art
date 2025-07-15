from PIL import Image
import numpy as np

ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

filepath = "pool1.jpg"
img = Image.open(filepath)
img_matrix = np.asarray(img)

intensity_matrix = []
for r in img_matrix:
    intensity_row = []
    for c in img_matrix:
        # luminosity with weighted avgs accounting for human perception
        intensity = 0.21 * c[0] + 0.72 * c[1] + 0.07 * c[2]
        intensity_row.append(intensity)
    intensity_matrix.append(intensity_row)
