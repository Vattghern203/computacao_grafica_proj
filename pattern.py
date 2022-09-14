import time

from PIL import Image, ImageOps

from colorsys import rgb_to_hsv

color_to_change = (255, 100, 0)

def max_min_hsv(sample):

    range_color = sample.getextrema()

    print(range_color[0, [0]], [1, [0]])

    return range_color[0, [0]], range_color[1, [0]]

def max_min_pattern(sample):
    
    range_color = sample.getextrema()

    print("Máximos e mínimos dos valores da amostra de cor: ", range_color)

    range_color_min = []
    range_color_max = []

    for color in range_color:
        range_color_min.append(color[0])
        range_color_max.append(color[1])

    tuple_color_max = tuple(map(int, range_color_max))
    tuple_color_min = tuple(map(int, range_color_min))

    return tuple_color_min, tuple_color_max

def rgb_pattern(sample, original):
    
    tuple_color_min, tuple_color_max = max_min_pattern(sample)

    print("Buscando valores entre {} e {}".format(tuple_color_min, tuple_color_max))

    pixel = original.load()

    for i in range(original.size[0]):
        for j in range(original.size[1]):

            if pixel[i, j] >= tuple_color_min and pixel[i, j] <= tuple_color_max:

                original.putpixel((i, j), color_to_change)

    converted_img = original.save("imgs/converted/RGB/img_converted({}).jpg".format(time.time()))

    original.show()

    return converted_img

def hsv_pattern(sample, original):

    tuple_color_min, tuple_color_max = max_min_pattern(sample)

    print("Buscando valores entre {} e {}".format(tuple_color_min, tuple_color_max))

    pixel = original.load()

    for i in range(original.size[0]):
        for j in range(original.size[1]):

            if pixel[i, j][0] >= tuple_color_min[0] and pixel[i, j][0] <= tuple_color_max[0]:

                original.putpixel((i, j), color_to_change)

    converted_img = original.save("imgs/converted/HSV/img_converted({}).jpg".format(time.time()))

    original.show()

    return converted_img

    

