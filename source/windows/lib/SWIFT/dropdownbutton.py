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
from PIL import ImageTk


class DropDownButton(Label):
    """ Drop Down Button widget.

    Parameters
    ----------
    master:
      Widget to place this widget into
    text:
      Default option of the drop down button (must be one of the options)
    command:
      Command to link this button to the dropdown menu
    """
    def __init__(self, master, text=None, command=None, **kwargs):

        self.text = text
        self.Arrows = ImageTk.PhotoImage(file="lib/SWIFT/bitmaps/Arrows.png")

        Label.__init__(self, master, bg='#4d4d4d', fg='grey90', relief=SOLID, bd=1,
                       text=self.text, compound='right', image=self.Arrows)

        self.bind('<Enter>', self._enter_btn)
        self.bind('<Leave>', self._leave_btn)
        self.bind('<ButtonRelease-1>', self._btn_release)

    def _enter_btn(self, event):
        self.configure(bg='grey40')

    def _leave_btn(self, event):
        self.configure(background='#4d4d4d')
        self.configure(fg='grey90')
        
    def _btn_release(self, event):
        self.configure(background='#4d4d4d')
        self.configure(fg='grey90')

    def get(self):
        return self.text
