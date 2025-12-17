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
from lib.SWIFT.colorchooserbutton import ColorChooserButton
from lib.SWIFT.colorchooser import ColorChooser
from lib.SWIFT.tooltip import ToolTip
from lib.core.render.renderer import render_photoimage


def property_view_ui(self):
    ## Panel
    self.Veiw_PropertyPnl = PropertyFrame(self.File_Properties_Panel,
                                          default=False,
                                          text="View")
    self.Veiw_PropertyPnl.pack(fill=X)

    ## Frame
    View_Frame = Frame(self.Veiw_PropertyPnl.interior, bg="#969696")
    View_Frame.pack(padx=2, pady=2, side=TOP, fill=X)

    ## Checkbutton
    self.ShowCheckeredBackground_Var = IntVar()
    self.ShowCheckeredBackground_Var.set(0)
    ShowCheckeredBg_Checkbutton = Checkbutton(View_Frame, text='Show checkered background',
                                              bg="#969696", selectcolor="#94afc9",
                                              activebackground="#969696",
                                              variable=self.ShowCheckeredBackground_Var,
                                              command=lambda: show_checkered_background(self))
    ShowCheckeredBg_Checkbutton.pack(padx=2, pady=2, anchor=W)
    ToolTip(ShowCheckeredBg_Checkbutton, "Show a checkered background behind the image")

    ## Frame
    PaddingColor_Frame = Frame(self.Veiw_PropertyPnl.interior, bg="#969696")
    PaddingColor_Frame.pack(padx=2, pady=2, side=TOP, fill=X)

    ## Label
    CanvasPaddingColor_Label = Label(PaddingColor_Frame, text='Padding Color: ',
                                     bg="#969696")
    CanvasPaddingColor_Label.grid(row=0, column=0, padx=2, pady=2)
    
    ## ColorChooser
    self.CanvasPaddingColor_Button = ColorChooserButton(PaddingColor_Frame)
    self.CanvasPaddingColor_Button.grid(row=0, column=1, padx=2, pady=2)
    ColorChooser(self.CanvasPaddingColor_Button, top=True, command=lambda: update_view(self))
    ToolTip(self.CanvasPaddingColor_Button, "Padding Color around the image")

    self.Veiw_PropertyPnl.update_width()


def update_view(self):
    try:
        self.canvas.configure(bg=str(self.CanvasPaddingColor_Button.cget("text")))
    except:
        pass

def show_checkered_background(self):
    if self.data.image != None:
        render_photoimage(self)

    ## if there is no image, we don't want this value to change
    else:
        self.ShowCheckeredBackground_Var.set(0)
        
