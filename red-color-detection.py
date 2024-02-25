import cv2
import numpy as np

# Load the image
image = cv2.imread('C:\\Users\\momen\\Documents\\11.jpg')

# Convert the image from BGR to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define lower and upper bounds for red color in HSV
lower_red1 = np.array([0, 100, 50])    # Lower bound for hue, saturation, and value
upper_red1 = np.array([10, 255, 255])   # Upper bound for hue, saturation, and value

lower_red2 = np.array([160, 100, 50])   # Lower bound for hue, saturation, and value
upper_red2 = np.array([180, 255, 255])  # Upper bound for hue, saturation, and value

# Create masks for the two red ranges
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

# Combine the masks to get the final mask
final_mask = cv2.bitwise_or(mask1, mask2)

# Bitwise-AND the mask with the original image to isolate the red regions
red_image = cv2.bitwise_and(image, image, mask=final_mask)

# Save the result
cv2.imwrite("C:\\Users\\momen\\Documents\\11.jpg", red_image)
