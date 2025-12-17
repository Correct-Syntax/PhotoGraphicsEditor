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
from PIL import Image, ImageFont, ImageDraw


def add_text(self, mainimage=None, x=0, y=0, text='', font=None, color='black',
             alignment='left'):
    """ Add Text on an image. """
    ## Prepare the image for the text
    DrawText = ImageDraw.Draw(mainimage)

    ## Draw the text
    DrawText.multiline_text((x, y), text, font=font, align=alignment, fill=(color))

    return mainimage



