# src/pipeline.py


from src.preprocessing import preprocess_image
from src.segmentation import segment_garment
from src.postprocessing import refine_mask
from src.utils import load_image, save_image

class GarmentMaskingPipeline:
    
    def process_image(self, image_path):
        # Load the image
        image = load_image(image_path)
        
        # Preprocess the image
        preprocessed_image = preprocess_image(image)
        
        # Perform segmentation
        mask = segment_garment(preprocessed_image)
        
        # Refine the mask
        refined_mask = refine_mask(mask)
        
        return refined_mask

    def save_mask(self, mask, output_path):
        save_image(mask, output_path)




