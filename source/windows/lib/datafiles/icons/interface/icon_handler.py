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
from PIL import ImageTk


def interface_icon_loader(self):
    ## interface
    self.OPENFILE_ICON = PhotoImage(file="lib/datafiles/icons/interface/Open_File.png")
    self.OPENFROMCLIPBOARD_ICON = PhotoImage(file="lib/datafiles/icons/interface/Open_From_Clipboard.png")
    self.SAVEFILE_ICON = PhotoImage(file="lib/datafiles/icons/interface/Save_File.png")
    self.SAVEFILEAS_ICON = PhotoImage(file="lib/datafiles/icons/interface/Save_File_As.png")
    self.SAVEBITMAPCOPY_ICON = PhotoImage(file="lib/datafiles/icons/interface/Save_Bitmap_Copy.png")
    self.UNDO_ICON = PhotoImage(file="lib/datafiles/icons/interface/Undo.png")
    self.REDO_ICON = PhotoImage(file="lib/datafiles/icons/interface/Redo.png")
    self.RESETIMAGE_ICON = PhotoImage(file="lib/datafiles/icons/interface/Reset.png")
    self.CLEARCACHE_ICON = PhotoImage(file="lib/datafiles/icons/interface/Clear_Cache.png")

    self.ROTATE90CLOCKWISE_ICON = PhotoImage(file="lib/datafiles/icons/interface/Rotate_90_Clockwise.png")
    self.ROTATE90COUNTERCLOCKWISE_ICON = PhotoImage(file="lib/datafiles/icons/interface/Rotate_90_Counter_Clockwise.png")
    self.ROTATE180_ICON = PhotoImage(file="lib/datafiles/icons/interface/Rotate_180.png")
    self.FLIPHORIZONTALLY_ICON = PhotoImage(file="lib/datafiles/icons/interface/Flip_Horizontally.png")
    self.FLIPVERTICALLY_ICON = PhotoImage(file="lib/datafiles/icons/interface/Flip_Vertically.png")


    self.PROPERTY_ICON = PhotoImage(file="lib/datafiles/icons/interface/Property.png")
    self.MODIFIER_ICON = PhotoImage(file="lib/datafiles/icons/interface/Modifier.png")

    ## topbar
    self.MAINPROGRAM_ICON = PhotoImage(file="lib/datafiles/icons/interface/Program.png")
    self.DOCUMENTATION_ICON = PhotoImage(file="lib/datafiles/icons/interface/Documentation.png")
    self.USERPREFERENCES_ICON = PhotoImage(file="lib/datafiles/icons/interface/UserPreferences.png")
    self.ABOUTPROGRAM_ICON = PhotoImage(file="lib/datafiles/icons/interface/AboutProgram.png")
