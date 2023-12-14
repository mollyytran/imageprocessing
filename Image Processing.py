"""
Molly Tran
CS 87B- Assignment 3 (Image Processing)
Original image is converted to grayscale then resized to a new dimension of 700X500.
"""

from PIL import Image


# Grayscale method: gets the width and height of the original image, creates a blank image, converts and sets each
# original Pixel into a gray Pixel, returns the grayscale image
def grayscale_image(original_image):
    width, height = original_image.size
    gray_image = Image.new('L', (width, height))

    for row in range(height):
        for col in range(width):
            original_pixel = original_image.getpixel((col, row))
            intensity_sum = sum(original_pixel)
            average_pixel = intensity_sum // 3
            gray_image.putpixel((col, row), average_pixel)

    return gray_image


# Resize method resizes the image based on the height and width passed to the method
def resize_image(filtered_image, new_width, new_height):
    resizedImage = filtered_image.resize((new_width, new_height))
    return resizedImage


# Main method opens the original image, calls the grayscale method, calls the resize method, displays and saves the
# new image
def main():
    original_image = Image.open('corgi.jpg')
    filtered_image = grayscale_image(original_image)
    new_image = resize_image(filtered_image, 700, 500)

    new_image.show()
    new_image.save('corgi2.jpg')


main()
