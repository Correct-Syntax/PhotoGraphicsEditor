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

from lib.core.urcache.cache import undo_action, redo_action, reset_actions


def property_undoredo_ui(self):
    ## Panel
    self.UndoRedo_PropertyPnl = PropertyFrame(self.File_Properties_Panel,
                                              text="Undo\Redo\Reset")
    self.UndoRedo_PropertyPnl.pack(fill=X)

    ## Frame
    UndoRedo_Frame = Frame(self.UndoRedo_PropertyPnl.interior, bg="#969696")
    UndoRedo_Frame.pack(padx=2, pady=2, side=TOP, fill=X)

    ## Undo Button
    Undo_Button = FlatButton(UndoRedo_Frame, text=' Undo ', width=90,
                             image=self.UNDO_ICON, compound='left',
                             command=lambda: undo_action(self))
    Undo_Button.pack(padx=2, pady=2, side=LEFT)
    ToolTip(Undo_Button, "Undo last action", "Shortcut: Ctrl+Z", wtype='FLATBUTTON')

    ## Redo Button
    Redo_Button = FlatButton(UndoRedo_Frame, text=' Redo ', width=90,
                             image=self.REDO_ICON, compound='left',
                             command=lambda: redo_action(self))
    Redo_Button.pack(padx=2, pady=2, side=RIGHT)
    ToolTip(Redo_Button, "Redo last action", "Shortcut: Ctrl+Y", wtype='FLATBUTTON')

    ## Frame
    Reset_Frame = Frame(self.UndoRedo_PropertyPnl.interior, bg="#969696")
    Reset_Frame.pack(padx=2, pady=2, side=TOP, fill=X)

    ## Reset Button
    Reset_Button = FlatButton(Reset_Frame, text=' Reset ', width=200, 
                             image=self.RESETIMAGE_ICON, compound='left',
                             command=lambda: reset_actions(self))
    Reset_Button.pack(padx=2, pady=2, side=TOP)
    ToolTip(Reset_Button, "Reset all actions and restore original image", "Shortcut: Shift+R",
            wtype='FLATBUTTON')


    self.UndoRedo_PropertyPnl.update_width()

