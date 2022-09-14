from PIL import Image, ImageOps

from pattern import hsv_pattern, rgb_pattern

from converterHSV import image_rgb_2_hsv

img_sample = Image.open(r"imgs/samples/color/cutted_foxy_sample_003.jpg").convert('RGB')

img_original = Image.open(r"imgs/samples/original/foxy_sample_004.jpg").convert('RGB')

# rgb_pattern(img_sample, img_original)

sample_hsv = image_rgb_2_hsv(img_sample)
img_hsv = image_rgb_2_hsv(img_original)

print(sample_hsv.getextrema())

hsv_pattern(sample_hsv, img_hsv)

