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
## (Tooltip concept inspired by IDLE's tooltip module)  

from tkinter import *
from tkinter.constants import *


class ToolTip(object):
    """ Create a tooltip for a widget.

    Parameters
    ----------
    widget:
      Widget to bind tooltip to
    text1:
      Main tooltip text
    text2:
      Separate area for other tooltip information, such as keyboard shortcuts
    codetext:
      Text explaining about the background code
    wtype:
      Type of widget the tooltip is for. Valid values are: DROPDOWNBUTTON or FLATBUTTON
    """
    def __init__(self, widget, text1=None, text2=None, codetext=None, wtype=None):

        ## variables
        self.widget = widget
        self.wtype = wtype
        self.text1 = text1
        self.text2 = text2
        self.codetext = codetext

        self.widget.bind("<Enter>", self._enter_widget)
        self.widget.bind("<Leave>", self._leave_widget)
            
        self.id = None
        self.tw = None

    def _enter_widget(self, event=None):
        ## we want it to be state=NORMAL
        if self.widget.cget("state") == DISABLED:
            return

        ## configure the highlight color of the widget
        if self.wtype == 'FLATBUTTON':
            self.widget.configure(bg='grey90')

        if self.wtype == 'DROPDOWNBUTTON':
            self.widget.configure(bg='grey40')
            
        else:
            pass
            
        self._schedule()

    def _leave_widget(self, event=None):
        ## configure the color of the widget back to normal
        if self.wtype == 'FLATBUTTON':
            self.widget.configure(bg='grey80')

        if self.wtype == 'DROPDOWNBUTTON':
            self.widget.configure(bg='#4d4d4d')
            
        else:
            pass
            
        self._unschedule()
        self._hide_tooltip()

    def _schedule(self):
        self._unschedule()
        ## wait 500 ms before showing the tooltip
        self.id = self.widget.after(500, self._show_tooltip)

    def _unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def _hide_tooltip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()

    def _show_tooltip(self, event=None):
        x = y = 0
        ## calculate where to have the tooltip appear
        try:
            x, y, cx, cy = self.widget.bbox("insert")
        except:
            pass
        
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        
        ## toplevel window
        self.tw = Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        
        ## we want it to have some transparency
        self.tw.attributes("-alpha", 0.85)

        ## frame with border - this should make it contrast from a dark background
        frame = Frame(self.tw, relief=GROOVE, bd=1, background='black')
        frame.pack()

        ## normal tooltip
        label = Label(
            frame,
            text=self.text1,
            justify='left',
            background='black',
            anchor='w',
            fg='white',
            relief='flat',
            borderwidth=10,
            wraplength=300
        )
        label.pack(side='top', fill='both')

        ## keyboard shortcut or warning
        if self.text2 != None:
            label2 = Label(
                frame,
                text=self.text2,
                justify='left',
                background='black',
                anchor='w',
                fg='white',
                relief='flat',
                borderwidth=10,
                wraplength=300,
                font=("Arial", 7)
            )
            label2.pack(side='top', fill='both')

        ## info regarding the code
        if self.codetext != None:
            label3 = Label(
                frame,
                text=self.codetext,
                justify='left',
                background='black',
                anchor='w',
                fg='white',
                relief='flat',
                borderwidth=10,
                wraplength=300,
                font=("Courier", 7)
            )
            label3.pack(side='bottom', fill='both')


## example code
if __name__ == '__main__':

    root = Tk()

    b = Button(root, text='Button Test')
    b.pack(fill=BOTH, expand=1)
    ToolTip(b, "Example Tooltip", codetext="code for tooltips")

    root.mainloop()
