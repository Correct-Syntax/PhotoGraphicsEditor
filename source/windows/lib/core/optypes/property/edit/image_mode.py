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

from PIL import Image
from lib.core.render.renderer import render_photoimage
from lib.core.urcache.handler import handle_cache


def convert_image_mode_rgb(self):
    if self.data.image!= None:
        ## Convert
        self.data.image = self.data.image.convert('RGB')

        ## Show image
        render_photoimage(self)

        ## Cache
        self.UndoQueue.cache_append(self.data.image)
        handle_cache(self, self.data.image)

        ## Update statusbar
        self.StatusBar_lbl.configure(text='Converted image mode to RGB')


def convert_image_mode_rgba(self):
    if self.data.image!= None:
        ## Convert
        self.data.image = self.data.image.convert('RGBA')

        ## Show image
        render_photoimage(self)

        ## Cache
        self.UndoQueue.cache_append(self.data.image)
        handle_cache(self, self.data.image)

        ## Update statusbar
        self.StatusBar_lbl.configure(text='Converted image mode to RGBA')


def convert_image_mode_l(self):
    if self.data.image!= None:
        ## Convert
        self.data.image = self.data.image.convert('L')

        ## Show image
        render_photoimage(self)

        ## Cache
        self.UndoQueue.cache_append(self.data.image)
        handle_cache(self, self.data.image)

        ## Update statusbar
        self.StatusBar_lbl.configure(text='Converted image mode to Grayscale (L)')
