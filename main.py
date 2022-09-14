from PIL import Image, ImageOps

from pattern import hsv_pattern, rgb_pattern

from converterHSV import image_rgb_2_hsv

img_sample = Image.open(r"imgs/samples/color/cutted_foxy_sample_003.jpg").convert('RGB')

img_original = Image.open(r"imgs/samples/original/foxy_sample_004.jpg").convert('RGB')

sample_hsv = image_rgb_2_hsv(img_sample)

original_hsv = image_rgb_2_hsv(img_original)

original_hsv.show().getextrema()

print(original_hsv.getbands())

print(sample_hsv.getextrema(), original_hsv.getextrema())



