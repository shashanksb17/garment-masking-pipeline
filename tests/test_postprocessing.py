# tests/test_postprocessing.py

import unittest
import numpy as np
from src.postprocessing import refine_mask

class TestPostprocessing(unittest.TestCase):

    def test_refine_mask(self):
        mask = np.zeros((100, 100), dtype=np.uint8)
        mask[30:70, 30:70] = 255
        
        refined_mask = refine_mask(mask)
        
        self.assertEqual(refined_mask.shape, mask.shape)

if __name__ == '__main__':
    unittest.main()
