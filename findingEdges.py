from PIL import ImageFilter

import time

def search_edges(img):

    img = img.convert("L")

    img = img.filter(ImageFilter.FIND_EDGES)

    img.save("imgs/converted/Edge/img_edge({}).jpg".format(time.time()))

    return img