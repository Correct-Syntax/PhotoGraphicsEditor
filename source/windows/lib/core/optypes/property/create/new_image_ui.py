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
from lib.SWIFT.colorchooser import ColorChooser
from lib.SWIFT.dropdownmenu import DropDownMenu
from lib.SWIFT.dropdownbutton import DropDownButton
from lib.SWIFT.propertyframe import PropertyFrame

from lib.core.optypes.property.create.new_image import create_new_image


def property_newimage_ui(self):
    ## Panel
    self.NewImage_PropertyPnl = PropertyFrame(self.Create_Properties_Panel,
                                              default=True,
                                              text="Create New Image")
    self.NewImage_PropertyPnl.pack(fill=X)

    ## New Image Size
    NewImageSize_Frame = Frame(self.NewImage_PropertyPnl.interior, bg="#969696")
    NewImageSize_Frame.pack(padx=2, pady=2, side=TOP)

    NewImageSize_Label = Label(NewImageSize_Frame, text='Dimensions: ',
                                bg="#969696")
    NewImageSize_Label.grid(row=0, column=0, padx=2, pady=2)
    
    self.NewImageSize_Dropdown = DropDownButton(NewImageSize_Frame, text='1024x1024')
    self.NewImageSize_Dropdown.grid(row=0, column=1, padx=1, pady=2)
    DropDownMenu(self.NewImageSize_Dropdown, chars=100,
                 options=[
                     'Icon 16x16',
                     '520x520',
                     '1024x1024',
                     '2048x2048',
                     'A3 3508x4960 ',
                     'A4 3508x2480',
                     'A5 2480x1748',
                     'A6 1748x1240',
                     'PAL 720x576',
                     'NTSC 720x486'
                     ],
                 commands={
                     'Icon 16x16': None,
                     '520x520': None,
                     '1024x1024': None,
                     '2048x2048': None,
                     'A3 3508x4960 ': None,
                     'A4 3508x2480': None,
                     'A5 2480x1748': None,
                     'A6 1748x1240': None,
                     'PAL 720x576': None,
                     'NTSC 720x486': None
                     },
                 flagtext="Image Dimensions")

    ## New Image Color
    NewImageColor_Frame = Frame(self.NewImage_PropertyPnl.interior, bg="#969696")
    NewImageColor_Frame.pack(padx=2, pady=2, side=TOP, fill=X)
    
    NewImageColor_Label = Label(NewImageColor_Frame, text='Fill Color: ',
                                bg="#969696")
    NewImageColor_Label.grid(row=0, column=0, padx=2, pady=2)
    
    self.NewImageColor_Button = ColorChooserButton(NewImageColor_Frame)
    self.NewImageColor_Button.grid(row=0, column=1, padx=2, pady=2)
    ColorChooser(self.NewImageColor_Button, command=lambda: update_newimage_ui(self))
    ToolTip(self.NewImageColor_Button, "Image fill color")

    ## New Image Mode
    NewImageMode_Frame = LabelFrame(self.NewImage_PropertyPnl.interior, text='Mode: ',
                                    bg="#969696")
    NewImageMode_Frame.pack(padx=2, pady=2, side=TOP, fill=X)

    self.NewImageMode_Var = StringVar()
    self.NewImageMode_Var.set('RGB')
    self.NewImgMode_RGB_Radiobtn = Radiobutton(NewImageMode_Frame, text='RGB', value='RGB',
                                               variable=self.NewImageMode_Var, selectcolor='#94afc9',
                                               bg="#969696", font=("Arial", 8),
                                               activebackground='#969696',
                                               command=lambda:update_newimage_ui(self))
    self.NewImgMode_RGB_Radiobtn.pack(padx=2, pady=2, anchor=W)
    ToolTip(self.NewImgMode_RGB_Radiobtn, "Create RGB image")

    self.NewImgMode_RGBA_Radiobtn = Radiobutton(NewImageMode_Frame, text='RGBA', value='RGBA',
                                                variable=self.NewImageMode_Var, selectcolor='#94afc9',
                                                bg="#969696", font=("Arial", 8),
                                                activebackground='#969696',
                                                command=lambda:update_newimage_ui(self))
    self.NewImgMode_RGBA_Radiobtn.pack(padx=2, pady=2, anchor=W)
    ToolTip(self.NewImgMode_RGBA_Radiobtn, "Create RGBA image")

    self.NewImgMode_L_Radiobtn = Radiobutton(NewImageMode_Frame, text='Greyscale (L)', value='L',
                                             variable=self.NewImageMode_Var, bg="#969696",
                                             font=("Arial", 8), selectcolor='#94afc9',
                                             activebackground='#969696',
                                             command=lambda:update_newimage_ui(self))
    self.NewImgMode_L_Radiobtn.pack(padx=2, pady=2, anchor=W)
    ToolTip(self.NewImgMode_L_Radiobtn, "Create Greyscale (L) image")

    ## Create New Image Button
    CreateNewImage_ButtonFrame = Frame(self.NewImage_PropertyPnl.interior, bg="#969696")
    CreateNewImage_ButtonFrame.pack(padx=2, pady=2, side=TOP, fill=X)
    
    CreateNewImage_Button = FlatButton(CreateNewImage_ButtonFrame, text=' Create New Image ',
                                       command=lambda: create_new_image(self))
    CreateNewImage_Button.pack(padx=2, pady=2, side=RIGHT)
    ToolTip(CreateNewImage_Button, "Create new image", wtype='FLATBUTTON')   

    self.NewImage_PropertyPnl.update_width()


def update_newimage_ui(self):
    if self.NewImageMode_Var.get() == 'RGB':
        self.NewImageColor_Button.configure(state=NORMAL)
        
    if self.NewImageMode_Var.get() == 'RGBA':
        self.NewImageColor_Button.configure(state=DISABLED)

    if self.NewImageMode_Var.get() == 'L':
        self.NewImageColor_Button.configure(state=DISABLED)

