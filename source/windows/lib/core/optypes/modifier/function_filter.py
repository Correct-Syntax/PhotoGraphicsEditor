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

import math
from decimal import *
from PIL import Image, ImageTransform, ImageEnhance, ImageFilter


def function_filter(self, mainimage, positions):
    ## build a list of the positions of the dots and number of points
    x_lst = []
    y_lst = []
    numberofpoints = 0
    for pos in positions:
        index = pos[1]
        ## we want the values to be integers to start with
        x_lst.append(round(index[0]))
        y_lst.append(round(index[1]))
        numberofpoints += 1

    ## build a list of the values
    lst = []
    for xpos in x_lst:
        for ypos in y_lst:
            ## divide the x position of the dots by the placing of
            ## the dots on the y axis
            position = float(xpos)/ypos
            lst.append(position)
        
    ## prepare the image
    img = mainimage
    width, height = img.size
    section = int(round(width/numberofpoints))

    ## split the image into sections
    sz = 0
    xvar = section
    imagesection_list = []
    for num in range(0, numberofpoints):
        im = img.transform(size=(section, height), method=Image.EXTENT,
                           data=(sz, 0, xvar, height))
        imagesection_list.append(im)
        xvar = xvar + section
        sz = sz + section

    ## enhance the image based on the values
    editedimage_list = []
    var = 0
    for image in imagesection_list:
        enh = ImageEnhance.Brightness(image)
        image = enh.enhance(lst[var])
        image = image.filter(ImageFilter.MedianFilter(size=3))
        editedimage_list.append(image)
        #image.save("test{}.png".format(var))
        var += 1

    ## create a new image and paste sections on the image
    sz = 0
    newimage = Image.new("RGB", (width, height))
    for image in editedimage_list:
        newimage.paste(image, (sz, 0))
        sz = sz + section

    return newimage
