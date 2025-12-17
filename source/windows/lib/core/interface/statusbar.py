## PhotoGraphics Editor 1.0.0 Copyright (C) 2019 Noah Rahm
##
## This program is free software: you can redistribute it and/or modify it 
## under the terms of the GNU General Public License as published by 
## the Free Software Foundation; either version 3 of the License, 
## or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful, 
## but WITHOUT ANY WARRANTY; without even the implied warranty 
## of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
##  
## See the GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License 
## along with this program. If not, see: http://www.gnu.org/licenses/

from tkinter import *
from tkinter.constants import *
from tkinter import ttk

#from lib.SWIFT.loadingbar import LoadingBar


def statusbar_ui(self):
    ## Main Frame
    Statusbar_Frame = Frame(self, bd=1, relief=RIDGE, bg="#7e7e7e")
    Statusbar_Frame.pack(padx=0, pady=0, side=BOTTOM, fill=X)

    ## Statusbar label
    self.StatusBar_lbl = Label(Statusbar_Frame, text='No image. Please open an image...',
                               bg="#7e7e7e")
    self.StatusBar_lbl.pack(pady=0, padx=2, side=LEFT)

    ## loading bar
##    BottomLoadingBar_Frame = Frame(Statusbar_Frame, bg="#7e7e7e")
##    BottomLoadingBar_Frame.pack(pady=0, padx=18, side=LEFT)
##    
##    self.BottomLoadingBar = LoadingBar(BottomLoadingBar_Frame)
##    self.BottomLoadingBar.reset()

    ## Cursor coordinates 
    CursorCoords_Frame = Frame(Statusbar_Frame, bg="#7e7e7e")
    CursorCoords_Frame.pack(pady=0, padx=15, side=RIGHT)
    
    ## X Coords
    X_Coords_lbl = Label(CursorCoords_Frame, text='X:', bg="#7e7e7e")
    X_Coords_lbl.grid(row=0, column=0)

    self.XCoords_lbl = Label(CursorCoords_Frame, text=' ', bg="#7e7e7e")
    self.XCoords_lbl.grid(row=0, column=1)

    ## Y Coords
    Y_Coords_lbl = Label(CursorCoords_Frame, text='Y:', bg="#7e7e7e")
    Y_Coords_lbl.grid(row=0, column=3)

    self.YCoords_lbl = Label(CursorCoords_Frame, text=' ', bg="#7e7e7e")
    self.YCoords_lbl.grid(row=0, column=4)

    ## Zoom amount
    ZoomAmount_Frame = Frame(Statusbar_Frame, bg="#7e7e7e")
    ZoomAmount_Frame.pack(pady=0, padx=15, side=RIGHT)
    
    Zoom_Amount_lbl = Label(ZoomAmount_Frame, text='Zoom: ', bg="#7e7e7e")
    Zoom_Amount_lbl.grid(row=0, column=0)

    self.ZoomAmount_lbl = Label(ZoomAmount_Frame, text='100%', bg="#7e7e7e")
    self.ZoomAmount_lbl.grid(row=0, column=1)
