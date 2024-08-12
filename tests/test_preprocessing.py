# tests/test_preprocessing.py

import unittest
import cv2
from src.preprocessing import preprocess_image

class TestPreprocessing(unittest.TestCase):

    def test_preprocess_image(self):
        image = cv2.imread('data/input/sample_image1.jpg')
        preprocessed_image = preprocess_image(image)
        
        self.assertEqual(preprocessed_image.shape, image.shape[:2])

if __name__ == '__main__':
    unittest.main()
