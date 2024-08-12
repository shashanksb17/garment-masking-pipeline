# # tests/test_segmentation.py

# import unittest
# import cv2
# from src.segmentation import segment_garment

# class TestSegmentation(unittest.TestCase):

#     def test_segment_garment(self):
#         image = cv2.imread('data/input/sample_image1.jpg', cv2.IMREAD_GRAYSCALE)
#         mask = segment_garment(image)
        
#         self.assertEqual(mask.shape, image.shape)

# if __name__ == '__main__':
#     unittest.main()

import cv2
import numpy as np
from src.segmentation import create_clothing_mask, apply_mask, load_model

def test_create_clothing_mask():
    model = load_model()
    image = cv2.imread('tests/test_image.jpg')  # Use a sample image
    mask = create_clothing_mask(image, model)
    assert mask is not None
    assert mask.shape == image.shape[:2]

def test_apply_mask():
    model = load_model()
    image = cv2.imread('tests/test_image.jpg')  # Use a sample image
    mask = create_clothing_mask(image, model)
    masked_image = apply_mask(image, mask)
    assert masked_image is not None
    assert masked_image.shape == image.shape
