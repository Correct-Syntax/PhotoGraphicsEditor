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

from PIL import Image, ImageOps

from lib.core.render.renderer import render_photoimage
from lib.core.urcache.handler import handle_cache


def flip_horizontally_transform(self):
    """ Transform image horizontally. """
    if self.data.image!= None:
        ## Transform image
        self.data.image = ImageOps.flip(self.data.image)

        ## Show image
        render_photoimage(self)

        ## Cache
        handle_cache(self, self.data.image)

        ## Update statusbar
        self.StatusBar_lbl.configure(text='Image was successfully flipped horizontally')


def flip_vertically_transform(self):
    """ Transform image vertically. """
    if self.data.image!= None:
        ## Transform image
        self.data.image = ImageOps.mirror(self.data.image)

        ## Show image
        render_photoimage(self)

        ## Cache
        handle_cache(self, self.data.image)

        ## Update statusbar
        self.StatusBar_lbl.configure(text='Image was successfully flipped vertically')


def rotate_90_clockwise_transform(self):
    """ Transform image 90 clockwise. """
    if self.data.image!= None:
        ## Transform image
        self.data.image = self.data.image.rotate(-90, expand=True)

        ## Show image
        render_photoimage(self)

        ## Cache
        handle_cache(self, self.data.image)

        ## Update statusbar
        self.StatusBar_lbl.configure(text='Image was successfully rotated 90 clockwise')


def rotate_90_counterclockwise_transform(self):
    """ Transform image 90 counter-clockwise. """
    if self.data.image!= None:
        ## Transform image
        self.data.image = self.data.image.rotate(90, expand=True)

        ## Show image
        render_photoimage(self)

        ## Cache
        handle_cache(self, self.data.image)

        ## Update statusbar
        self.StatusBar_lbl.configure(text='Image was successfully rotated 90 counter-clockwise')


def rotate_180_transform(self):
    """ Transform image 180. """
    if self.data.image!= None:
        ## Transform image
        self.data.image = self.data.image.rotate(180, expand=True)

        ## Show image
        render_photoimage(self)

        ## Cache
        handle_cache(self, self.data.image)

        ## Update statusbar
        self.StatusBar_lbl.configure(text='Image was successfully rotated 180')

