import colorsys

from PIL import Image, ImageOps

import time

def image_rgb_2_hsv(img):
        r, g, b = img.split()
        Hdat = []
        Sdat = []
        Vdat = []

        for rd, gn, bl in zip(r.getdata(), g.getdata(), b.getdata()):
            h, s, v = colorsys.rgb_to_hsv(rd / 255., gn / 255., bl / 255.)
            Hdat.append(int(h * 255.))
            Sdat.append(int(s * 255.))
            Vdat.append(int(v * 255.))

        r.putdata(Hdat)
        g.putdata(Sdat)
        b.putdata(Vdat)

        print(len(Hdat))
    
        hsv_image = Image.merge('RGB', (r, g, b))

        hsv_image.save("imgs/converted/HSV/img_hsv({}).jpg".format(time.time()))

        return hsv_image