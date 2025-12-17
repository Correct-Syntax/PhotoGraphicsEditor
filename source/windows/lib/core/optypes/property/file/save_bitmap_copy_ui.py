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

from lib.SWIFT.propertyframe import PropertyFrame
from lib.SWIFT.tooltip import ToolTip
from lib.SWIFT.flatbutton import FlatButton

from lib.core.optypes.property.file.save_bitmap_copy import save_bitmap_copy


def property_save_bitmap_copy_ui(self):
    ## Panel
    self.SaveBitmapCopy_PropertyPnl = PropertyFrame(self.File_Properties_Panel,
                                                    default=False,
                                                    text="Save Bitmap Copy")
    self.SaveBitmapCopy_PropertyPnl.pack(fill=X)


    SaveBitmapCopy_Button = FlatButton(self.SaveBitmapCopy_PropertyPnl.interior,
                                       compoun='left', image=self.SAVEBITMAPCOPY_ICON,
                                       width=200, text=' Save Bitmap Copy',
                                       command=lambda: save_bitmap_copy(self))
    SaveBitmapCopy_Button.pack(padx=2, pady=2, side=TOP)
    ToolTip(SaveBitmapCopy_Button, "Save a bmp copy of the current image to the default location on your hard drive", 
            wtype='FLATBUTTON')

    self.SaveBitmapCopy_PropertyPnl.update_width()
