from PIL import Image
import numpy as np

filepath = "IMG_1965.jpeg"
img = Image.open(filepath)

# print(f"Image Size = {img.size}")
# print(f"Image Mode = {img.mode}")

img_array = np.asarray(img)
print(img_array.shape)