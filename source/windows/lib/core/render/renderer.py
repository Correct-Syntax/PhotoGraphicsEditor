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

"""
'self.data.image' is the variable assigned to the *current image*. This
is the image which is rendered and shown on the canvas.

The basic flow of self.image.data in the program is:

1. self.data.image starts out as equal to None. This way, the program
knows that an image has not been created or opened.

2. self.data.image becomes the image that is either opened or created
within the program.

> Image information is extracted from the image for later use

> A copy of self.data.image is saved for the reset function

> A copy of self.data.image is pushed into the undo/redo stack

> self.data.image is rendered and shown on the canvas.

3. [This loop happens every time the image is edited or zoomed and
continues until the image is saved or the user quits the program.]:

The self.data.image is edited -> a copy of self.data.image is pushed
into the undo/redo stack -> the ui is updated -> self.data.image is
rendered and shown on the canvas -> other updates are done, if needed
"""

import copy
from tkinter import *
from tkinter.constants import *
from PIL import Image, ImageTk


def render_photoimage(self):
    """ Renders the image for the show_image function to use. """
    imageWidth = self.data.image.size[0] 
    imageHeight = self.data.image.size[1]

    ## If the zoom value does not equal the default value
    if self.zoom_value != 1.0:
        try:
            ## Resize the image to the correct dimensions
            self.zoom_image = self.data.image.resize((int(imageWidth*self.zoom_value),
                                                      int(imageHeight*self.zoom_value)))
        ## if the zoom is to its limit we can pass
        except ValueError:
            pass
            
        ## Render alpha channel (checkered) background
        render_checkered_background(self)
    
    else:
        ## The image does not need to be resized
        self.zoom_image = self.data.image

        ## Render alpha channel (checkered) background
        render_checkered_background(self)

    ## Render the image on the canvas
    self.rendered_img = ImageTk.PhotoImage(self.zoom_image)
    self.canvas.create_image(0, 0, anchor=NW, image=self.rendered_img)


def render_checkered_background(self):
    """ Renders a checkered background image if the setting is turned on. """
    if self.ShowCheckeredBackground_Var.get() == 0:
        self.canvas.delete('checkered_bg')
        
    if self.ShowCheckeredBackground_Var.get() == 1:
        ## Resize the image to the same dimensions as the actual image
        self.checkeredbackground_image = Image.open(
            "lib/datafiles/icons/other/Checkered.png"
            ).resize((int(self.data.image.size[0]*self.zoom_value),
                      int(self.data.image.size[1]*self.zoom_value)))

        ## Render the image on the canvas
        self.checkeredbackground_image = ImageTk.PhotoImage(self.checkeredbackground_image)
        self.canvas.create_image(0, 0, anchor=NW, image=self.checkeredbackground_image, tag='checkered_bg')


def render_image_preview(self, previewimage):
    """ Renders the image preview for the Preview Docker. """
    ## copy the image
    preview_image = previewimage.copy()

    ## get the image size
    ImageWidth = preview_image.size[0] 
    ImageHeight = preview_image.size[1]
    
    ## Resize the image to the correct dimensions
    if ImageWidth == ImageHeight:
        self.data.previewimage = preview_image.resize((200, 200))

    elif ImageWidth > ImageHeight:
        self.data.previewimage = preview_image.resize((200, int(round(float(ImageHeight) * 200/ImageWidth))))

    else:
        self.data.previewimage = preview_image.resize((int(round(float(ImageWidth) * 200/ImageHeight)), 200))


def show_image_preview(self, preview_image):
    """ Shows the image preview on the Preview Docker canvas. """
    ## Create the preview
    self.FinalPreviewImage = ImageTk.PhotoImage(self.data.previewimage)
    self.ImagePreview_Canvas.create_image(0, 0, anchor=NW, image=self.FinalPreviewImage)
