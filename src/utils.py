# src/utils.py

import cv2

def load_image(image_path):
    # Load an image from the specified path
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    return image

def save_image(image, output_path):
    # Save an image to the specified path
    cv2.imwrite(output_path, image)
