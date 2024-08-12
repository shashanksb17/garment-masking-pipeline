# src/segmentation.py

import cv2
import numpy as np

def segment_garment(image):
    # Threshold the image to create a binary mask
    _, mask = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    return mask

