from PIL import Image, ImageOps
from findingEdges import search_edges

from pattern import hsv_pattern, rgb_pattern, max_min_pattern_hsv

from converterHSV import image_rgb_2_hsv

# Carrega as imgens, amostra e original, respectivamente.
img_sample = Image.open(r"imgs/samples/color/cutted_foxy_sample_001.jpg").convert("RGB")

img_original = Image.open(r"imgs/samples/original/foxy_sample_002.jpg").convert('RGB')

# Chama as funções

# HSV
sample_hsv = image_rgb_2_hsv(img_sample)

original_hsv = image_rgb_2_hsv(img_original)

# Edge

hsv_pattern(sample_hsv, original_hsv)

print(sample_hsv.getextrema())

img_edge = search_edges(img_original)


