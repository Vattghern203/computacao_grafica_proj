import time

import math

from PIL import Image, ImageOps

from colorsys import rgb_to_hsv

def rgb_to_hsv_value(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0

    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn

    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100

    return h, s, v

def max_min_pattern(sample):
    
    range_color = sample.getextrema()

    print("Máximos e mínimos dos valores da amostra de cor HSV: ", range_color)

    range_color_min = []
    range_color_max = []

    for color in range_color:
        range_color_min.append(color[0])
        range_color_max.append(color[1])

    tuple_color_max = tuple(map(int, range_color_max))
    tuple_color_min = tuple(map(int, range_color_min))

    return tuple_color_min, tuple_color_max


def max_min_pattern_hsv(sample_hsv):

    range_color = sample_hsv.getextrema()

    range_color_min = []
    range_color_max = []

    for color in range_color:
        range_color_min.append(color[0])
        range_color_max.append(color[1])

    rmin, gmin, bmin = range_color_min
    rmax, gmax, bmax = range_color_max

    range_min = rgb_to_hsv_value(rmin, gmin, bmin)
    range_max = rgb_to_hsv_value(rmax, gmax, bmax)

    return range_min, range_max

def rgb_pattern(sample, original):

    color_to_change = (255, 100, 0)
    
    tuple_color_min, tuple_color_max = max_min_pattern(sample)

    print("Buscando valores entre {} e {}".format(tuple_color_min, tuple_color_max))

    pixel = original.load()

    for i in range(original.size[0]):
        for j in range(original.size[1]):

            if pixel[i, j] >= tuple_color_min and pixel[i, j] <= tuple_color_max:

                original.putpixel((i, j), color_to_change)

    original.save("imgs/converted/RGB/img_rgb_scanned({}).jpg".format(time.time()))

    return original

def hsv_pattern(sample, original):

    color_to_change = (39, 100, 100)

    pixel = original.load()

    for i in range(original.size[0]):
        for j in range(original.size[1]):

            if pixel[i, j] >= (0, 0, 0) and pixel[i, j] <= (40, 100, 100):

                original.putpixel((i, j), color_to_change)

    original.save("imgs/converted/HSV/img_hsv_scanned({}).jpg".format(time.time()))

    return original

    

