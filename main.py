# main.py

import os
from src.pipleline import GarmentMaskingPipeline

def main():
    input_dir = 'data/input'
    output_dir = 'data/output'
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Initialize the masking pipeline
    pipeline = GarmentMaskingPipeline()

    # Process each image in the input directory
    for image_name in os.listdir(input_dir):
        input_path = os.path.join(input_dir, image_name)
        output_path = os.path.join(output_dir, image_name)

        print(f"Processing {image_name}...")
        mask = pipeline.process_image(input_path)
        
        # Save the output mask
        pipeline.save_mask(mask, output_path)
        print(f"Mask saved to {output_path}")

if __name__ == '__main__':
    main()




