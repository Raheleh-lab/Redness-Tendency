import cv2
import numpy as np

# Load the image
image = cv2.imread('C:\\Users\\momen\\Desktop\\appl\\8.jpg')

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

# Calculate the redness tendency as a ratio of red pixels to the total number of pixels
red_pixel_count = np.sum(final_mask == 255)  # Count white pixels in the final mask (red)
total_pixel_count = final_mask.size  # Total number of pixels in the mask

redness_tendency = red_pixel_count / total_pixel_count

# Print the redness tendency
print(f"Redness Tendency: {redness_tendency:.2%}")
#  You can also save the red regions as a separate image
# red_image = cv2.bitwise_and(image, image, mask=final_mask)
# cv2.imwrite("C:\\Users\\momen\\Documents\\Output\\redness\\red2-detected.jpg", red_image)