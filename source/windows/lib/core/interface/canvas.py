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


def canvas_ui(self):
    ## Main frame
    Canvas_Frame = Frame(self, borderwidth=2, relief=GROOVE, bg="grey50")
    Canvas_Frame.pack(padx=4, pady=4, side=RIGHT)

    ## Canvas
    self.canvas = Canvas(Canvas_Frame, background='grey55', width=1100,
                         highlightcolor="grey60", highlightthickness=1,
                         height=740, scrollregion=(0, 0, 0, 0),
                         relief=GROOVE, bd=1)
    
    # Scrollbars
    self.xscrollbar = Scrollbar(Canvas_Frame, orient=HORIZONTAL,
                                command=self.canvas.xview)
    self.yscrollbar = Scrollbar(Canvas_Frame, orient=VERTICAL,
                                command=self.canvas.yview)
    self.canvas.configure(yscrollcommand=self.yscrollbar.set,
                          xscrollcommand=self.xscrollbar.set)
    self.xscrollbar.pack(padx=1, pady=1, side=BOTTOM, fill=X)
    self.yscrollbar.pack(padx=1, pady=1, side=RIGHT, fill=Y)

    ## Scale x
    scale_x = Frame(Canvas_Frame, bg="grey50")
    scale_x.pack(side=TOP)
    self.scale_x_canvas = Canvas(scale_x, width=1090, height=12,
                                 highlightthickness=0, bg="grey50")
    self.scale_x_canvas.pack(side=LEFT)

    for i in range(1100):
        if i%10 == 0:
            self.scale_x_canvas.create_line(i,8,i,15, width=1, fill='black')

    ## Scale y
    scale_y = Frame(Canvas_Frame, bg="grey50")
    scale_y.pack(side=LEFT)
    self.scale_y_canvas = Canvas(scale_y, height=750, width=12,
                                 highlightthickness=0, bg="grey50")
    self.scale_y_canvas.pack(side=TOP)

    for i in range(750):
        if i%10 == 0:
            self.scale_y_canvas.create_line(0,i,5,i, width=1, fill='black')

    self.canvas.pack(side=LEFT)


def update_coordinates(self, event):
    ## Update scales
    self.scale_x_canvas.delete('cursor')
    self.scale_y_canvas.delete('cursor')
    self.scale_x_canvas.create_line(event.x,0,event.x,15, width=2,
                                    fill='grey20', tag='cursor')
    self.scale_y_canvas.create_line(0,event.y,15,event.y, width=2,
                                    fill='grey20', tag='cursor')

    ## Update coordinates
    x = event.x
    y = event.y
    self.XCoords_lbl.configure(text=x)
    self.YCoords_lbl.configure(text=y)
