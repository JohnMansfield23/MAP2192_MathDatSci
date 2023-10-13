# -*- coding: utf-8 -*-
"""ProblemSet2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FTgzsr0Ioe-LRQtVdu5iYNicL2sCLNgw
"""



import numpy as np
import matplotlib.pyplot as plt
import requests
from PIL import Image
import cv2

# Load image
URL = 'https://1000logos.net/wp-content/uploads/2019/12/Florida-Atlantic-Owls-Logo-1994.png'
response = requests.get(URL, stream=True)
img = Image.open(response.raw).convert("RGB")

# Plot
plt.imshow(img)
plt.title("Original Image")
plt.axis('off')
plt.show()

# Convert to numpy array and show shape
img_array = np.array(img)
print("Shape:", img_array.shape)

# Resize image to 224x224
resized_image = cv2.resize(img_array, (224, 224))

# Plot the reshaped image
plt.imshow(resized_image)
plt.title("Resized Image")
plt.axis('off')
plt.show()

# Convert to grayscale
grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_RGB2GRAY)

# Show shape
print("Grayscale Shape:", grayscale_image.shape)

# Plot grayscale image
plt.imshow(grayscale_image, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')
plt.show()

# Randomly generate 10 n x n filters
filter_size = 3
filters = [np.random.randn(filter_size, filter_size) for _ in range(10)]

fig, axs = plt.subplots(10, 2, figsize=(10, 30))
for i, filt in enumerate(filters):
    feature_map = cv2.filter2D(grayscale_image, -1, filt)

    axs[i, 0].imshow(filt, cmap='gray')
    axs[i, 0].set_title(f"Filter {i + 1}")
    axs[i, 0].axis('off')

    axs[i, 1].imshow(feature_map, cmap='gray')
    axs[i, 1].set_title(f"Feature Map {i + 1}")
    axs[i, 1].axis('off')

plt.tight_layout()
plt.show()

























