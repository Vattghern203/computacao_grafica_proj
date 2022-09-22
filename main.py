from PIL import Image, ImageOps
from findingEdges import search_edges

from pattern import hsv_pattern, rgb_pattern, max_min_pattern_hsv

from converterHSV import image_rgb_2_hsv

# Carrega as imgens, amostra e original, respectivamente.
img_sample = Image.open(r"imgs/samples/color/foxy_sample_000.png").convert('RGB')

img_original = Image.open(r"imgs/samples/original/foxy_sample_004.jpg").convert('RGB')

img_sample.show()

# Chama as funções

# HSV
sample_hsv = image_rgb_2_hsv(img_sample)

original_hsv = image_rgb_2_hsv(img_original)

# Edge

rgb_pattern(img_sample, img_original)

print(img_sample.getextrema())

img_edge = search_edges(img_original)

img_edge.show()


