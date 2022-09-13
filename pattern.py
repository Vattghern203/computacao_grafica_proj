import time

from PIL import Image, ImageOps

def getting_patterns(sample, original):
    range_color = sample.getextrema()

    print("Máximos e mínimos dos valores RGB da amostra de cor: ", range_color)

    range_color_min = []
    range_color_max = []

    for color in range_color:
        range_color_min.append(color[0])
        range_color_max.append(color[1])

    tuple_color_max = tuple(map(int, range_color_max))
    tuple_color_min = tuple(map(int, range_color_min))

    print("Buscando valores entre {} e {}".format(tuple_color_min, tuple_color_max))

    color_to_change = (255, 100, 0)

    pixel = original.load()

    for i in range(original.size[0]):
        for j in range(original.size[1]):

            if pixel[i, j] >= tuple_color_min and pixel[i, j] <= tuple_color_max:

                original.putpixel((i, j), color_to_change)

    converted_img = original.save("imgs/converted/RGB/img_converted({}).jpg".format(time.time()))

    original.show()

    return converted_img
