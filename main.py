from colorsys import rgb_to_hsv

from PIL import Image, ImageOps

import time

from pattern import getting_patterns

img_sample = Image.open(r"imgs/samples/cutted_foxy_sample_003.jpg").convert('RGB')

img_original = Image.open(r"imgs/samples/foxy_sample_004.jpg")

getting_patterns(img_sample, img_original)

