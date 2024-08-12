from tensorflow.keras.models import load_model
from src.pipleline import GarmentMaskingPipeline


def main():
    model_path = 'models/garment_masking_model.h5'  # Update with the actual path to your model
    input_dir = 'data/input/'
    output_dir = 'data/output/'

    model = load_model(model_path)
    pipeline = GarmentMaskingPipeline(model, input_dir, output_dir)
    pipeline.process_images()

if __name__ == "__main__":
    main()