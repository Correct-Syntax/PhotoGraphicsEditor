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

from lib.core.render.renderer import render_photoimage


def handle_zooming(self, event):
    """ Handles the zoom functionality. """
    if type(event) == str:
        x = float(event)
        self.zoom_value = x
    
    else:
        if event.delta > 0:
            if self.zoom_value < 2.5:
                self.zoom_value += 0.1
            x = self.zoom_value

        else:
            if self.zoom_value > 0.1:
                self.zoom_value -= 0.1
            x = self.zoom_value
    
    ## Show image
    render_photoimage(self)

    ## Make the scrollregion to be the same as the image size
    self.canvas.configure(scrollregion=(0, 0, self.data.image.size[0]*x,
                                        self.data.image.size[1]*x))

    ## Update zoom amount label
    self.ZoomAmount_lbl.configure(text = '{}%'.format(round(x*100)))

