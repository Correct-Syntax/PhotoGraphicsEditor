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

from lib.core.optypes.property.file.file_output import save_file, save_file_as


def property_fileoutput_ui(self):
    ## Panel
    self.SaveImageFile_PropertyPnl = PropertyFrame(self.File_Properties_Panel,
                                                   default=False,
                                                   text ="Image Output")
    self.SaveImageFile_PropertyPnl.pack(fill=X)


    ## Image Output Frame
    ImageOutput_Frame = Frame(self.SaveImageFile_PropertyPnl.interior, bg="#969696")
    ImageOutput_Frame.pack(padx=2, pady=2, side=TOP, fill=X)

    ## Save Image Button
    SaveImage_Button = FlatButton(ImageOutput_Frame, text=' Save... ',
                                      image=self.SAVEFILE_ICON, compound='left',
                                      command=lambda: save_file(self))
    SaveImage_Button.pack(padx=12, pady=2, side=RIGHT)
    ToolTip(SaveImage_Button, "Overwrites the original image file with the current image",
            "Shortcut: Ctrl+S", wtype='FLATBUTTON')

    ## Save Image As Button
    SaveImageAs_Button = FlatButton(ImageOutput_Frame, text=' Save As... ',
                                      image=self.SAVEFILEAS_ICON, compound='left',
                                      command=lambda: save_file_as(self))
    SaveImageAs_Button.pack(padx=12, pady=2, side=LEFT)
    ToolTip(SaveImageAs_Button, "Save image file as a separate file", "Shortcut: Shift+S",
            wtype='FLATBUTTON')

    self.SaveImageFile_PropertyPnl.update_width()

