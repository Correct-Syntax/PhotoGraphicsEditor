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
## Includes code from Miguel Martinez Lopez

from tkinter import *
from tkinter.constants import *
from tkinter import ttk
from PIL import ImageTk

from lib.SWIFT.tooltip import ToolTip


class ModifierFrame(Frame):
    """ Modifier Frame widget.

    Parameters
    ----------
    master:
      Widget to place this widget into
    text:
      Title text of the collapsible frame
    width:
      Width of frame
    height:
      Height of the top title label (default is the best in most cases)
    icon:
      Icon to be displayed beside the title label
    closecommand:
      Command to be run when the user closes the collapsible frame
    default:
      Default for whether of not the collapsible frame is open to start with.
      Valid values are: True or False
    """
    def __init__(self, master, text=None, width=0, height=16, icon=None,
                 closecommand=None, default=True):
        Frame.__init__(self, master, bg="#969696")

        self._is_opened = False
        self._default = default
        self._titletext = " {}".format(text)
        self._height = height
        self._width = width
        self._closecommand = closecommand

        ## Separator
        SeparatorStyle = ttk.Style()
        SeparatorStyle.configure("Line.TSeparator", background="black")
        Separator = ttk.Separator(self, orient=HORIZONTAL, style="Line.TSeparator")
        Separator.pack(pady=4, padx=4, side=TOP, fill=X)

        ## Container Frame
        self._containerFrame = Frame(self, width=width, height=height, bg="#969696")
        self._containerFrame.pack(expand=True, fill=X, pady=(7, 0))
        self.interior = Frame(self._containerFrame, bg="#969696")

        ## Collapse Button
        self.IconOpen = ImageTk.PhotoImage(file="lib/SWIFT/bitmaps/Arrow_Open.png")
        self.IconClose = ImageTk.PhotoImage(file="lib/SWIFT/bitmaps/Arrow_Closed.png")
        self._collapseButton = Label(self, borderwidth=0, image=self.IconClose, bg="#969696")
        ToolTip(self._collapseButton, "Expand/collapse modifier UI")
        self._collapseButton.place(in_= self._containerFrame, x=10, y=-(12//2), anchor=N+W, bordermode="ignore")
        self._collapseButton.bind("<Button-1>", lambda event: self.toggle())

        ## Main icon for the Collapsible Frame
        if icon != None:
            self.Icon = ImageTk.PhotoImage(file=icon)
            self._Icon = Label(self, image=self.Icon, bg="#969696")
            self._place_caption(self._Icon, 0, 10, 12)

        else:
            self._Icon = Label(self, borderwidth=0, text='    ', bg="#969696")
            self._place_caption(self._Icon, 0, 10, 12)   

        ## Written caption (label) for the Collapsible Frame
        self._captionLabel = Label(self, anchor=W, text=self._titletext, bg="#969696", font=("Arial", 9))
        ToolTip(self._captionLabel, "Modifier name: {}".format(text))
        self._place_caption(self._captionLabel, 0, 10, 28)
        self._captionLabel.bind("<Button-1>", lambda event: self.toggle())

        ## Close button
        self.IconDestroy = ImageTk.PhotoImage(file="lib/SWIFT/bitmaps/Destroy.png")
        self._Close = Label(self, image=self.IconDestroy, bg="#969696")
        ToolTip(self._Close, "Remove from modifier stack")
        self._place_caption(self._Close, 0, 10, 182)
        self._Close.bind("<Button-1>", lambda event: self.close_command())

        ## have the frame default to being open 
        if self._default == True:
            self.open()

    def update_width(self, width=None):
        self.after(0, lambda width=width:self._update_width(width))
                                     
    def _place_caption(self, lbl, caption_separation, icon_x, width_of_icon):
        self.update()
        x = caption_separation + icon_x + width_of_icon
        y = -(lbl.winfo_reqheight()//2)
        lbl.place(in_= self._containerFrame, x=x, y=y, anchor=N+W, bordermode="ignore")

    def _update_width(self, width):
        self.update()
        if width is None:
            width=self.interior.winfo_reqwidth()
        if isinstance(4, (list, tuple)):
            width += 4[0] + 4[1]
        else:
            width += 2*4
        width = max(self._width, width)
        self._containerFrame.configure(width=width)
                 
    def open(self):
        self._collapseButton.configure(image=self.IconOpen)
        self._containerFrame.configure(height=self.interior.winfo_reqheight())
        self.interior.pack(expand=True, ipady=4, fill=X, padx=4, pady=16)
        self._is_opened = True
                 
    def close(self):
        self.interior.pack_forget()
        self._containerFrame.configure(height=self._height)
        self._collapseButton.configure(image=self.IconClose)
        self._is_opened = False
                 
    def toggle(self):
        if self._is_opened:
            self.close()
        else:
            self.open()

    def close_command(self):
        self.destroy()
        
        if self._closecommand != None:
            self._closecommand()
                                          
