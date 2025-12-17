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

from lib.core.optypes.property.file.image_info import update_imageinfo


def property_imageinfo_ui(self):       
    ## Panel
    self.ImageInfo_PropertyPnl = PropertyFrame(self.File_Properties_Panel,
                                               default=False,
                                               text ="Image Information")
    self.ImageInfo_PropertyPnl.pack(fill=X)

    ## Frame
    ImageInfo_Frame = Frame(self.ImageInfo_PropertyPnl.interior, bg="#969696")
    ImageInfo_Frame.pack(padx=2, pady=2, side=TOP, fill=X)

    ## Name
    ImageName_Lbl = Label(ImageInfo_Frame, text='File Name:', justify='left',
                          bg="#969696", font=("Arial Bold", 8))
    ImageName_Lbl.pack(padx=2, pady=2)
    
    self.ImageInfo_ImageName_Lbl = Label(ImageInfo_Frame, text='',
                                          bg="#969696", justify='left',
                                          wraplength=190, font=("Arial", 8))
    self.ImageInfo_ImageName_Lbl.pack(padx=2, pady=2)
    
    ## Size in pixels
    ImageSize_Lbl = Label(ImageInfo_Frame, text='Size In Pixels:', justify='left',
                          bg="#969696", font=("Arial Bold", 8))
    ImageSize_Lbl.pack(padx=2, pady=2)
    
    self.ImageInfo_ImageSize_Lbl = Label(ImageInfo_Frame, text='', bg="#969696",
                                         justify='left', font=("Arial", 8))
    self.ImageInfo_ImageSize_Lbl.pack(padx=2, pady=2)

    ## Mode
    ImageMode_Lbl = Label(ImageInfo_Frame, text='Mode:', bg="#969696",
                           justify='left', font=("Arial Bold", 8))
    ImageMode_Lbl.pack(padx=2, pady=2)
    
    self.ImageInfo_ImageMode_Lbl = Label(ImageInfo_Frame, text='', bg="#969696",
                                         justify='left', font=("Arial", 8))
    self.ImageInfo_ImageMode_Lbl.pack(padx=2, pady=2)

    ## File Size
    ImageFileSize_Lbl = Label(ImageInfo_Frame, text='File Size:', bg="#969696",
                               justify='left', font=("Arial Bold", 8))
    ImageFileSize_Lbl.pack(padx=2, pady=2)
    
    self.ImageInfo_ImageFileSize_Lbl = Label(ImageInfo_Frame, text='', bg="#969696",
                                             justify='left', font=("Arial", 8))
    self.ImageInfo_ImageFileSize_Lbl.pack(padx=2, pady=2)

    ## Frame
    ImageInfo_ButtonFrame = Frame(self.ImageInfo_PropertyPnl.interior, bg="#969696")
    ImageInfo_ButtonFrame.pack(padx=2, pady=2, side=TOP, fill=X)
    
    ## Update Button
    Update_Button = FlatButton(ImageInfo_ButtonFrame, text=' Update ',
                               command=lambda: update_imageinfo(self))
    Update_Button.pack(padx=12, pady=2, side=RIGHT)
    ToolTip(Update_Button, "Update image information", wtype='FLATBUTTON')

    self.ImageInfo_PropertyPnl.update_width()
