
# Garment Masking Pipeline

## Overview

The **Garment Masking Pipeline** is a tool designed to automatically segment and mask garments in images. This pipeline can be used in fashion technology, e-commerce, and any other domain that requires accurate garment masking from images.

## Features

- **Automated Garment Segmentation**: Automatically identify and mask garments in images.
- **Flexible Input/Output**: Supports various image formats for input and output.
- **Customizable Pipeline**: Easily extend and customize the pipeline to suit specific requirements.
- **Efficient Processing**: Optimized for batch processing of large datasets.

## Requirements

Before running the pipeline, ensure you have the following dependencies installed:

- Python 3.8+
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)
- [TensorFlow](https://www.tensorflow.org/) or [PyTorch](https://pytorch.org/) (depending on your model backend)
- [scikit-learn](https://scikit-learn.org/)
- [Pillow](https://python-pillow.org/)

You can install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/shashanksb17/garment-masking-pipeline.git
   cd garment-masking-pipeline
   ```

2. **Install Dependencies**

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Pre-trained Models**

   Download and place the pre-trained model files in the `models/` directory. You can train your own models or use publicly available garment segmentation models.

## Usage

To run the garment masking pipeline, use the following command:

```bash
python run_pipeline.py --input_dir /path/to/input/images --output_dir /path/to/output/masks
```

### Arguments

- `--input_dir`: Path to the directory containing the input images.
- `--output_dir`: Path to the directory where the output masks will be saved.
- `--model_path` (optional): Path to the pre-trained model file. Defaults to the model in the `models/` directory.
- `--batch_size` (optional): Batch size for processing images. Default is 32.

## Customization

### Modifying the Pipeline

You can customize the pipeline by modifying the `pipeline.py` file. This allows you to add or remove steps, change the model, or adjust the processing logic.

### Training Your Own Model

To train your own garment segmentation model, refer to the `train_model.py` script. Make sure to update the `model_path` argument in `run_pipeline.py` to point to your trained model.

## Contributing

Contributions are welcome! If you find a bug, have a feature request, or want to contribute code, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The segmentation models used in this pipeline are based on [TensorFlow](https://www.tensorflow.org/) and [PyTorch](https://pytorch.org/).
- Special thanks to the open-source community for providing valuable resources and tools.

