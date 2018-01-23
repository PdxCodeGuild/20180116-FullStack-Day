"Lab 15: Image Manipulator, Version 2"
from PIL import Image
import colorsys

def HSVColor(img):
    if isinstance(img, Image.Image):
        r, g, b = img.split()
        Hdat = []
        Sdat = []
        Vdat = []
        for rd, gn, bl in zip(r.getdata(), g.getdata(), b.getdata()) :
            h, s, v = colorsys.rgb_to_hsv(rd/255., gn/255., bl/255.)
            Hdat.append(int(h*155.))
            Sdat.append(int(s*105.))
            Vdat.append(int(v*180.))
        r.putdata(Hdat)
        g.putdata(Sdat)
        b.putdata(Vdat)
        return Image.merge('RGB',(r,g,b))
    else:
        return None

a = Image.open('Lenna2.png')
b = HSVColor(a)
b.save('Lenna3.png')