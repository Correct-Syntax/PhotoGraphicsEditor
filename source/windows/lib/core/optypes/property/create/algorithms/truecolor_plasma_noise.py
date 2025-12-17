## This code is Copyright (C) 2019 Noah Rahm
##
## This program is free software: you can redistribute it and/or modify it 
## under the terms of the GNU General Public License as published by 
## the Free Software Foundation; either version 3 of the License, 
## or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful, 
## but WITHOUT ANY WARRANTY; without even the implied warranty 
## of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License 
## along with this program. If not, see: http://www.gnu.org/licenses/
##
## Contributor(s): Noah Rahm
## This code of this algorithm is Copyright 2016 FB36

import random
from PIL import Image


def create_truecolorplasma_noise(self, dimensions):
    imgx = dimensions[0]
    imgy = dimensions[1]
    image = Image.new("RGB", (imgx, imgy))
    self.pixels = image.load()
    mx = imgx - 1
    my = imgy - 1
    f = 2.0 ## roughness

    putpixel(self, 0, 0, random.randint(0, 255),
             random.randint(0, 255), random.randint(0, 255))
    putpixel(self, mx, 0, random.randint(0, 255),
             random.randint(0, 255), random.randint(0, 255))
    putpixel(self, mx, my, random.randint(0, 255),
             random.randint(0, 255), random.randint(0, 255))
    putpixel(self, 0, my, random.randint(0, 255),
             random.randint(0, 255), random.randint(0, 255))

    j = -1
    while True:
        j += 1
        j2 = 2 ** j
        jx = float(mx) / j2; jy = float(my) / j2
        
        if jx < 1 and jy < 1:
            break
        
        for i in range(j2):
            y0 = i * jy; y1 = y0 + jy; y = y0 + jy / 2.0        
            for k in range(j2):
                x0 = k * jx; x1 = x0 + jx; x = x0 + jx / 2.0
            
                a = getpixel(self, x0, y0); b = getpixel(self, x1, y0)
                c = getpixel(self, x0, y1); d = getpixel(self, x1, y1)

                putpixel(self, x, y, (a[0] + b[0] + c[0] + d[0]) / 4.0,
                         (a[1] + b[1] + c[1] + d[1]) / 4.0, (a[2] + b[2] + c[2] + d[2]) / 4.0)
                putpixel(self, x, y0, (a[0] + b[0]) / 2.0 + jx * (random.random() - .5) * f,
                         (a[1] + b[1]) / 2.0 + jx * (random.random() - .5) * f,
                         (a[2] + b[2]) / 2.0 + jx * (random.random() - .5) * f)
                putpixel(self, x0, y, (a[0] + c[0]) / 2.0 + jy * (random.random() - .5) * f,
                         (a[1] + c[1]) / 2.0 + jy * (random.random() - .5) * f,
                         (a[2] + c[2]) / 2.0 + jy * (random.random() - .5) * f)
                putpixel(self, x1, y, (b[0] + d[0]) / 2.0 + jy * (random.random() - .5) * f,
                         (b[1] + d[1]) / 2.0 + jy * (random.random() - .5) * f,
                         (b[2] + d[2]) / 2.0 + jy * (random.random() - .5) * f) 
                putpixel(self, x, y1, (c[0] + d[0]) / 2.0 + jx * (random.random() - .5) * f,
                         (c[1] + d[1]) / 2.0 + jx * (random.random() - .5) * f,
                         (c[2] + d[2]) / 2.0 + jx * (random.random() - .5) * f)

    return image


def putpixel(self, x, y, r, g, b):
    self.pixels[int(round(x)), int(round(y))] = (int(round(r)),
                                                 int(round(g)),
                                                 int(round(b)))


def getpixel(self, x, y):
    return self.pixels[int(round(x)), int(round(y))]
