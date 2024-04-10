from stegano import lsb
from PIL import Image
import os

def convert_to_png(input_file, output_file):
    if input_file.lower().endswith('.jpg') or input_file.lower().endswith('.jpeg'):

        img = Image.open(input_file)
        png_output_file = output_file
        if not output_file.lower().endswith('.png'):
            png_output_file = os.path.splitext(output_file)[0] + '.png'

        img.save(png_output_file, format='PNG')
        print(f"Converted '{input_file}' to PNG format: '{png_output_file}'")
    else:
        print(f"The input file '{input_file}' is not a JPEG image. No conversion needed.")

convert_to_png('input.jpg', 'output.jpg')