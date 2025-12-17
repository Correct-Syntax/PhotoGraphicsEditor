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

from lib.core.urcache.cache import clear_cache


def property_cache_ui(self):
    ## Panel
    self.Cache_PropertyPnl = PropertyFrame(self.File_Properties_Panel,
                                           default=False,
                                           text="Cache")
    self.Cache_PropertyPnl.pack(fill=X)

    ## Clear Cache Button
    ClearCache_Button = FlatButton(self.Cache_PropertyPnl.interior,
                                   text=' Clear Cache ', width=200,
                                   image=self.CLEARCACHE_ICON, compound='left',
                                   command=lambda: clear_cache(self))
    ClearCache_Button.pack(padx=2, pady=2, side=TOP)
    ToolTip(ClearCache_Button, "Clear the undo/redo cache", """WARNING: Clears all actions in the
undo and redo cache""", """Useful for avoiding memory issues
with high-resolution images""", wtype='FLATBUTTON')

    ## Cache Frame
    Cache_Frame = Frame(self.Cache_PropertyPnl.interior, bg="#969696")
    Cache_Frame.pack(padx=2, pady=2, side=TOP, fill=X)

    ## Listbox
    self.Cache_Listbox = Listbox(
        Cache_Frame,
        bg='grey40',
        fg='white',
        disabledforeground='white',
        font=("Calibri", 7),
        highlightbackground='grey40',
        highlightcolor='grey40',
        height=self.UndoQueue.cache_maxsize(),
        relief=GROOVE,
        activestyle='dotbox',
        selectbackground='#94afc9',
        selectforeground='black'
        )
    self.Cache_Listbox.pack(side=TOP, fill=X)

    # insert a blank label
    self.Cache_Listbox.insert(END, '<empty>')

    self.Cache_PropertyPnl.update_width()
