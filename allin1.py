import cv2
import numpy as np

# Read Image
img = cv2.imread('/Users/saurabh/SAURABH_PROGRAMS/data/ganesh.jpg')

# Write Image (Save Original)
cv2.imwrite('original.jpg', img)

# Convert to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Complement of Image (For Color Images)
complement = 255 - img

# Histogram Equalization (For Each Channel)
channels = cv2.split(img)
equalized_channels = [cv2.equalizeHist(ch) for ch in channels]
equalized = cv2.merge(equalized_channels)

# Smoothing (Gaussian Blur on Original Image)
blurred = cv2.GaussianBlur(img, (5,5), 0)

# Sharpening (Using Kernel)
sharpening_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpened = cv2.filter2D(img, -1, sharpening_kernel)

# Display Results
cv2.imshow('Original', img)
cv2.imshow('Complement', complement)
cv2.imshow('Histogram Equalized', equalized)
cv2.imshow('Blurred', blurred)
cv2.imshow('Sharpened', sharpened)


cv2.waitKey(0)
cv2.destroyAllWindows()
