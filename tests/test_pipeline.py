# tests/test_pipeline.py

import unittest
from src.pipeline import GarmentMaskingPipeline
import os

class TestGarmentMaskingPipeline(unittest.TestCase):

    def test_pipeline(self):
        pipeline = GarmentMaskingPipeline()
        input_path = 'data/input/sample_image1.jpg'
        output_path = 'data/output/sample_image1_mask.jpg'
        
        mask = pipeline.process_image(input_path)
        pipeline.save_mask(mask, output_path)
        
        self.assertTrue(os.path.exists(output_path))

if __name__ == '__main__':
    unittest.main()
