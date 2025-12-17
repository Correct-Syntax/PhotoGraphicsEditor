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

from tkinter import *
from tkinter.constants import *
from tkinter import ttk
from PIL import Image, ImageChops


def layer_image(self, mainimage, layerimage, blendmode):
    """ Layer a given image over another image with a blend mode. """
    try:
        ## See if the size of the layer image matches the main image
        if mainimage.size == layerimage.size:
            main_image = mainimage.convert("RGB")
            layer_image = layerimage.convert("RGB")

        else:
            ## Resize the layer image first
            layer_image = layerimage.resize(size=(mainimage.size[0],
                                                  mainimage.size[1])).convert("RGB")
            main_image = mainimage.convert("RGB")


        ## Apply the layer effect
        if blendmode == 'Add':
            image = ImageChops.add(main_image, layer_image)

        if blendmode == 'Add Mod':
            image = ImageChops.add_modulo(main_image, layer_image)

        if blendmode == 'Subtract':
            image = ImageChops.subtract(main_image, layer_image)

        if blendmode == 'Subtract Mod':
            image = ImageChops.subtract_modulo(main_image, layer_image)

        if blendmode == 'Multiply':
            image = ImageChops.multiply(main_image, layer_image)

        if blendmode == 'Screen':
            image = ImageChops.screen(main_image, layer_image)

        if blendmode == 'Difference':
            image = ImageChops.difference(main_image, layer_image)
            
        if blendmode == 'Darker':
            image = ImageChops.darker(main_image, layer_image)

        if blendmode == 'Lighter':
            image = ImageChops.lighter(main_image, layer_image)

        return image

    except AttributeError:
        pass
        
