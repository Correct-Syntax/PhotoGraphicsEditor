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

from lib.core.optypes.property.edit.image_mode import convert_image_mode_rgb
from lib.core.optypes.property.edit.image_mode import convert_image_mode_rgba
from lib.core.optypes.property.edit.image_mode import convert_image_mode_l


def property_imagemode_ui(self):
    ## Panel
    self.ImageMode_PropertyPnl = PropertyFrame(self.Edit_Properties_Panel,
                                               default=False,
                                               text="Image Mode")
    self.ImageMode_PropertyPnl.pack(fill=X)


    ## Image Mode Frame
    ImageMode_Frame = Frame(self.ImageMode_PropertyPnl.interior, bg="#969696")
    ImageMode_Frame.pack(padx=2, pady=2, side=TOP, fill=X)

    self.ImageMode_Var = StringVar()
    self.ImageMode_Var.set('RGB')
    self.ImgMode_RGB_Radiobtn = Radiobutton(ImageMode_Frame, text='RGB', value='RGB',
                                            variable=self.ImageMode_Var, selectcolor='#94afc9',
                                            bg="#969696", font=("Arial", 8),
                                            activebackground='#969696',
                                            command=lambda:convert_imagemode(self))
    self.ImgMode_RGB_Radiobtn.pack(padx=2, pady=2, anchor=W)
    ToolTip(self.ImgMode_RGB_Radiobtn, "Convert image mode to RGB")

    self.ImgMode_RGBA_Radiobtn = Radiobutton(ImageMode_Frame, text='RGBA', value='RGBA',
                                             variable=self.ImageMode_Var, selectcolor='#94afc9',
                                             bg="#969696", font=("Arial", 8),
                                             activebackground='#969696',
                                             command=lambda:convert_imagemode(self))
    self.ImgMode_RGBA_Radiobtn.pack(padx=2, pady=2, anchor=W)
    ToolTip(self.ImgMode_RGBA_Radiobtn, "Convert image mode to RGBA")

    self.ImgMode_L_Radiobtn = Radiobutton(ImageMode_Frame, text='Greyscale (L)', value='L',
                                          variable=self.ImageMode_Var, bg="#969696",
                                          font=("Arial", 8), selectcolor='#94afc9',
                                          activebackground='#969696',
                                          command=lambda:convert_imagemode(self))
    self.ImgMode_L_Radiobtn.pack(padx=2, pady=2, anchor=W)
    ToolTip(self.ImgMode_L_Radiobtn, "Convert image mode to Greyscale (L)")

    self.ImageMode_PropertyPnl.update_width()


def convert_imagemode(self):
    ## Get the value of the radiobuttons
    if self.ImageMode_Var.get() == 'RGB':
        convert_image_mode_rgb(self)

    if self.ImageMode_Var.get() == 'RGBA':
        convert_image_mode_rgba(self)

    if self.ImageMode_Var.get() == 'L':
        convert_image_mode_l(self)
  
