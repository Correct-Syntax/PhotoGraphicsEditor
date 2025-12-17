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

from lib.core.optypes.property.file.file_input import open_file, open_from_clipboard


def property_fileinput_ui(self):
    ## Panel
    self.OpenImageFile_PropertyPnl = PropertyFrame(self.File_Properties_Panel,
                                                   text="Image Input")
    self.OpenImageFile_PropertyPnl.pack(fill=X)
    
    ## Image Input Frame
    ImageInput_Frame = Frame(self.OpenImageFile_PropertyPnl.interior, bg="#969696")
    ImageInput_Frame.pack(padx=0, pady=0, side=TOP, fill=X)

    ## Open Image From Clipboard Button
    OpenImageFromClipboard_Button = FlatButton(ImageInput_Frame, text=' From Clipboard ',
                                               image=self.OPENFROMCLIPBOARD_ICON, compound='left',
                                               command=lambda: open_from_clipboard(self))
    OpenImageFromClipboard_Button.pack(padx=2, pady=2, side=RIGHT)
    ToolTip(OpenImageFromClipboard_Button, "Open image file from the clipboard",
            wtype='FLATBUTTON')

    ## Open Image Button
    OpenImagePath_Button = FlatButton(ImageInput_Frame, text=' Open... ',
                                      image=self.OPENFILE_ICON, compound='left',
                                      command=lambda: open_file(self))
    OpenImagePath_Button.pack(padx=2, pady=2, side=LEFT)
    ToolTip(OpenImagePath_Button, "Open an image file", "Shortcut: Ctrl+O",
            wtype='FLATBUTTON')
    
    self.OpenImageFile_PropertyPnl.update_width()
