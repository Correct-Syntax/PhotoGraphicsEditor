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

from lib.SWIFT.tooltip import ToolTip
from lib.SWIFT.flatbutton import FlatButton
from lib.SWIFT.colorchooserbutton import ColorChooserButton
from lib.SWIFT.dropdownmenu import DropDownMenu
from lib.SWIFT.dropdownbutton import DropDownButton
from lib.SWIFT.propertyframe import PropertyFrame

from lib.core.optypes.property.create.noise_image import create_noise_image


def property_noiseimage_ui(self):
    ## Panel
    self.NoiseImage_PropertyPnl = PropertyFrame(self.Create_Properties_Panel,
                                                default=True,
                                                text="Create Noise Image")
    self.NoiseImage_PropertyPnl.pack(fill=X)

    ## Noise Image Size
    NoiseImageSize_Frame = Frame(self.NoiseImage_PropertyPnl.interior, bg="#969696")
    NoiseImageSize_Frame.pack(padx=2, pady=2, side=TOP)

    NoiseImageSize_Label = Label(NoiseImageSize_Frame, text='Dimensions: ',
                                 bg="#969696")
    NoiseImageSize_Label.grid(row=0, column=0, padx=2, pady=2)
    
    self.NoiseImageSize_Dropdown = DropDownButton(NoiseImageSize_Frame, text='520x520')
    self.NoiseImageSize_Dropdown.grid(row=0, column=1, padx=1, pady=2)
    DropDownMenu(self.NoiseImageSize_Dropdown, chars=100,
                 options=[
                     'Icon 16x16',
                     '520x520',
                     '1024x1024',
                     'PAL 720x576',
                     'NTSC 720x486'
                     ],
                 commands={
                     'Icon 16x16': None,
                     '520x520': None,
                     '1024x1024': None,
                     'PAL 720x576': None,
                     'NTSC 720x486': None
                     },
                 flagtext="Image Dimensions")


    ## Noise Type 
    NoiseType_Frame = Frame(self.NoiseImage_PropertyPnl.interior, bg="#969696")
    NoiseType_Frame.pack(padx=2, pady=2, side=TOP)

    NoiseType_Label = Label(NoiseType_Frame, text='Noise Type: ',
                            bg="#969696")
    NoiseType_Label.grid(row=0, column=0, padx=2, pady=2)
    
    self.NoiseType_Dropdown = DropDownButton(NoiseType_Frame, text='Truecolor Plasma')
    self.NoiseType_Dropdown.grid(row=0, column=1, padx=1, pady=2)
    DropDownMenu(self.NoiseType_Dropdown, chars=110, width=15,
                 options=[
                     'Truecolor Plasma',
                     'Perlin (Cloud)',
                     'Perlin (Marble)',
                     'Perlin (Wood)'
                     ],
                 commands={
                     'Truecolor Plasma': None,
                     'Perlin (Cloud)': None,
                     'Perlin (Marble)': None,
                     'Perlin (Wood)': None
                     },
                 flagtext="Noise Type")

    ## Create Noise Image Button
    CreateNoiseImage_ButtonFrame = Frame(self.NoiseImage_PropertyPnl.interior, bg="#969696")
    CreateNoiseImage_ButtonFrame.pack(padx=2, pady=2, side=TOP, fill=X)
    
    CreateNoiseImage_Button = FlatButton(CreateNoiseImage_ButtonFrame, text=' Create Noise Image ',
                                       command=lambda: create_noise_image(self))
    CreateNoiseImage_Button.pack(padx=2, pady=2, side=RIGHT)
    ToolTip(CreateNoiseImage_Button, "Create noise image", wtype='FLATBUTTON')   

    self.NoiseImage_PropertyPnl.update_width()
