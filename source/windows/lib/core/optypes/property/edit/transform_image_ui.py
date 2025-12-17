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

from lib.SWIFT.propertyframe import PropertyFrame
from lib.SWIFT.tooltip import ToolTip
from lib.SWIFT.flatbutton import FlatButton

from lib.core.optypes.property.edit.transform_image import flip_horizontally_transform
from lib.core.optypes.property.edit.transform_image import flip_vertically_transform
from lib.core.optypes.property.edit.transform_image import rotate_90_clockwise_transform
from lib.core.optypes.property.edit.transform_image import rotate_90_counterclockwise_transform
from lib.core.optypes.property.edit.transform_image import rotate_180_transform


def property_transformimage_ui(self):
    ## Panel
    self.TransformImage_PropertyPnl = PropertyFrame(self.Edit_Properties_Panel,
                                                    default=True,
                                                    text="Transform Image")
    self.TransformImage_PropertyPnl.pack(fill=X)

    ## Transform Image Frame
    TransformImage_Frame = Frame(self.TransformImage_PropertyPnl.interior, bg="#969696")
    TransformImage_Frame.pack(padx=2, pady=2, side=TOP, fill=X)

    ## Rotate 90 Clockwise Button
    Rotate90clockwise_Button = FlatButton(TransformImage_Frame, text=' Rotate 90° ',
                                          image=self.ROTATE90CLOCKWISE_ICON, compound='left',
                                          width=200,
                                          command=lambda: rotate_90_clockwise_transform(self))
    Rotate90clockwise_Button.pack(padx=2, pady=2, side=TOP)
    ToolTip(Rotate90clockwise_Button, "Rotate the image 90 degrees clockwise",
            wtype='FLATBUTTON')

    ## Rotate 90 Counterclockwise Button
    Rotate90counterclockwise_Button = FlatButton(TransformImage_Frame, text=' Rotate -90° ',
                                                 image=self.ROTATE90COUNTERCLOCKWISE_ICON, compound='left',
                                                 width=200,
                                                 command=lambda: rotate_90_counterclockwise_transform(self))
    Rotate90counterclockwise_Button.pack(padx=2, pady=2, side=TOP)
    ToolTip(Rotate90counterclockwise_Button, "Rotate the image 90 degrees counterclockwise",
            wtype='FLATBUTTON')

    ## Rotate 180 Button
    Rotate180_Button = FlatButton(TransformImage_Frame, text=' Rotate 180° ',
                                  image=self.ROTATE180_ICON, compound='left',
                                  width=200,
                                  command=lambda: rotate_180_transform(self))
    Rotate180_Button.pack(padx=2, pady=2, side=TOP)
    ToolTip(Rotate180_Button, "Rotate the image 180 degrees", wtype='FLATBUTTON')
    
    ## Flip Horizontally Button
    FlipHorizontally_Button = FlatButton(TransformImage_Frame, text=' Flip Horizontally ',
                                         image=self.FLIPHORIZONTALLY_ICON, compound='left',
                                         width=200,
                                         command=lambda: flip_horizontally_transform(self))
    FlipHorizontally_Button.pack(padx=2, pady=2, side=TOP)
    ToolTip(FlipHorizontally_Button, "Flip the image horizontally along the x axis",
            wtype='FLATBUTTON')

    ## Flip Vertically Button
    FlipVertically_Button = FlatButton(TransformImage_Frame, text=' Flip Vertically ',
                                       image=self.FLIPVERTICALLY_ICON, compound='left',
                                       width=200,
                                       command=lambda: flip_vertically_transform(self))
    FlipVertically_Button.pack(padx=2, pady=2, side=TOP)
    ToolTip(FlipVertically_Button, "Flip the image vertically along the y axis",
            wtype='FLATBUTTON')


    self.TransformImage_PropertyPnl.update_width()
