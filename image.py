import os
import numpy as np
from skimage.io import imread, imsave
from skimage.color import rgb2gray
import helper
from PIL import Image
import matplotlib.pyplot as plt

def process(directoryName):
    output_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(directoryName):
        if filename.lower().endswith(('.jpg', '.png')):
            file_path = os.path.join(directoryName, filename)
            img = imread(file_path)
            img_new = rgb2gray(img)
            
            # Save grayscale image using Pillow for memory efficiency
            grayscale_img = Image.fromarray((img_new * 255).astype(np.uint8))
            
            # Generate a random file name for the modified image
            random_name = helper.generateRandomName()
            output_file_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}-{random_name}_modified.jpeg")
            grayscale_img.save(output_file_path)

            # Optionally close the figure if you were using matplotlib
            plt.close('all')
        else:
            continue
