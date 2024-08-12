# tests/test_utils.py

import unittest
import cv2
from src.utils import load_image, save_image

class TestUtils(unittest.TestCase):

    def test_load_image(self):
        image = load_image('data/input/sample_image1.jpg')
        self.assertIsNotNone(image)

    def test_save_image(self):
        image = cv2.imread('data/input/sample_image1.jpg')
        save_image(image, 'data/output/test_image.jpg')
        self.assertTrue(os.path.exists('data/output/test_image.jpg'))

if __name__ == '__main__':
    unittest.main()
