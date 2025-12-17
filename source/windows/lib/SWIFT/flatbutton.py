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
from tkinter import font

class FlatButton(Label):
    """ Button widget.

    Parameters
    ----------
    master:
      Widget to place this widget into
    text:
      Text on the button
    command:
      Callback for button

    other parameters can be specified, which are inherited from the label widget
    """
    def __init__(self, master, text=None, command=None, **kwargs):
        f = font.Font(family="Arial", size=9, weight=NORMAL)
        Label.__init__(self, master, text=text, bd=1, relief=SOLID, bg='grey80',
                       highlightthickness=0, font=f, **kwargs)

        self.master = master
        self.command = command
        
        self.bind('<Enter>', self._enter_btn)
        self.bind('<FocusIn>', self._enter_btn)
        self.bind('<Leave>', self._leave_btn)
        self.bind('<FocusOut>', self._leave_btn)
        
        self.bind('<ButtonPress-1>', self._btn_press)
        self.bind('<ButtonRelease-1>', self._btn_release)
        self.bind('<Key-space>', self._activate_btn)

    def _enter_btn(self, event):
        self.configure(bg='grey90')

    def _leave_btn(self, event):
        self.configure(background='grey80')
        self.configure(fg='black')

    def _btn_press(self, event):
        self.configure(background='grey50')
        self.configure(fg='grey95')

    def _btn_release(self, event):
        self.configure(background='grey80')
        self.configure(fg='black')
        self.command()

    def _activate_btn(self, event):
        self.command()
