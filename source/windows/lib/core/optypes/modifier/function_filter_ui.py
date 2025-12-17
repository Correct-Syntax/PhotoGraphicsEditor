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

import copy
from tkinter import *
from tkinter.constants import *
from PIL import Image

from lib.SWIFT.modifierframe import ModifierFrame
from lib.SWIFT.tooltip import ToolTip
from lib.SWIFT.flatbutton import FlatButton
from lib.SWIFT.dropdownmenu import DropDownMenu
from lib.SWIFT.dropdownbutton import DropDownButton
from lib.SWIFT.openfiledialog import OpenFileDialog
from lib.core.render.renderer import render_photoimage, render_image_preview, show_image_preview
from lib.core.urcache.handler import handle_cache
from lib.core.optypes.modifier.function_filter import function_filter

    
def modifier_functionfilter_ui(self):
    ## Panel
    self.FunctionFilter_ModifierPnl = ModifierFrame(self.Main_Modifier_Panel,
                                                    text="Function Filter", default=True,
                                                    icon="lib/datafiles/icons/interface/FunctionFilterModifier.png",
                                                    closecommand=lambda:close_functionfilter_modifier(self))
    self.FunctionFilter_ModifierPnl.pack(fill=X)

    ## Modifier Button Frame
    Modifier_ButtonFrame = Frame(self.FunctionFilter_ModifierPnl.interior, bg="#969696",
                                 bd=1, relief=GROOVE)
    Modifier_ButtonFrame.pack(padx=2, pady=4, side=TOP, fill=X)

    Apply_Button = FlatButton(Modifier_ButtonFrame, text=' Apply ', width=10,
                              command=lambda: apply_function_filter(self))
    Apply_Button.pack(padx=2, pady=2, side=LEFT)
    ToolTip(Apply_Button, "Apply function filter modifier", wtype='FLATBUTTON')

    Refresh_Button = FlatButton(Modifier_ButtonFrame, text=' Refresh ', width=10, 
                                command=lambda: preview_function_filter(self))
    Refresh_Button.pack(padx=2, pady=2, side=RIGHT)
    ToolTip(Refresh_Button, "Refresh preview of function filter modifier", wtype='FLATBUTTON')

    ## frame
    FunctionFilter_Frame = Frame(self.FunctionFilter_ModifierPnl.interior, bg="#969696")
    FunctionFilter_Frame.pack(fill=BOTH)

    ## create the function filter canvas
    self.FunctionFilter_Canvas = Canvas(FunctionFilter_Frame, width=200,
                                        height=200, bg='white')
    self.FunctionFilter_Canvas.pack(side=TOP)

    ## variables
    self.dotSize = 10
    self.Offset_X = 10
    self.Offset_Y = 10
    self.Box = (10, 10, 190, 190)
    self.StartDot = None
    self.EndDot = None
    self.Dots = []
    self.Lines = []
    self.Positions = {}
    self.org_pos = []

    ## draw the grid
    for x in range(10, 190, 10):
        self.FunctionFilter_Canvas.create_line(x, 10, x, 190, fill="grey80")
    for y in range(10, 190, 10):
        self.FunctionFilter_Canvas.create_line(10, y, 190, y, fill="grey80")
        
    ## draw a box around the edges of the canvas (top, left, right, down)
    self.FunctionFilter_Canvas.create_line(self.Box[0] - 1, self.Box[1] - 1,
                                           self.Box[2] + 1, self.Box[1] - 1,
                                           fill="grey60")
    self.FunctionFilter_Canvas.create_line(self.Box[0] - 1, self.Box[1] - 1,
                                           self.Box[1] - 1, self.Box[2] + 1,
                                           fill="grey60")
    self.FunctionFilter_Canvas.create_line(self.Box[2] + 1, self.Box[1] - 1,
                                           self.Box[2] + 1, self.Box[3] + 1,
                                           fill="grey60")
    self.FunctionFilter_Canvas.create_line(self.Box[0] - 1, self.Box[2] + 1,
                                           self.Box[2] + 1, self.Box[3] + 1,
                                           fill="grey60")

    ## draw start and end dot
    self.StartDot = self.FunctionFilter_Canvas.create_oval(translate_canvas_coords(self, 0, 185), activefill="grey40", fill="black")
    self.Dots.append(self.StartDot)
    self.Positions[self.StartDot] = (10, 185)
    
    self.EndDot = self.FunctionFilter_Canvas.create_oval(translate_canvas_coords(self, 185, 0), activefill="grey40", fill="black")
    self.Dots.append(self.EndDot)
    self.Positions[self.EndDot] = (185, 10)
    self.Positions = sort_dots(self)

    ## draw the line
    self.Line = self.FunctionFilter_Canvas.create_line(find_dot_coord(self, self.StartDot),
                                                       find_dot_coord(self, self.EndDot),
                                                       smooth=True, splinesteps=16, fill="black")
    self.Lines.append(self.Line)

    ## canvas bindings
    self.FunctionFilter_Canvas.tag_bind(self.StartDot, "<B1-Motion>", lambda event: onlyUpAndDown(self, self.StartDot, event))
    self.FunctionFilter_Canvas.tag_bind(self.EndDot, "<B1-Motion>", lambda event: onlyUpAndDown(self, self.EndDot, event))
    self.FunctionFilter_Canvas.bind("<Control-Button-1>", lambda event: new_dot(self, event))

    ## binding to update preview
    self.FunctionFilter_Canvas.bind("<ButtonRelease-1>", lambda event: preview_function_filter(self))

    ## frame
    FunctionFilterButton_Frame = Frame(FunctionFilter_Frame, bg="#969696")
    FunctionFilterButton_Frame.pack(padx=2, fill=BOTH)

    ## labels
    FunctionFilter_lbl1 = Label(FunctionFilterButton_Frame,
                                text='Left-click on a point to move', bg="#969696")
    FunctionFilter_lbl1.pack()

    FunctionFilter_lbl2 = Label(FunctionFilterButton_Frame,
                                text='Ctrl+click to add a point', bg="#969696")
    FunctionFilter_lbl2.pack()

    FunctionFilter_lbl3 = Label(FunctionFilterButton_Frame,
                                text='Right-click on a point to delete', bg="#969696")
    FunctionFilter_lbl3.pack()

    ## button
    ResetFunctionFilterCanvas_Button = FlatButton(FunctionFilterButton_Frame,
                                                  text=' Reset Function Filter ',
                                                  command=lambda: reset_canvas(self))
    ResetFunctionFilterCanvas_Button.pack(pady=4)
    ToolTip(ResetFunctionFilterCanvas_Button, "Reset the function filter back to the default position",
            wtype='FLATBUTTON')

    ## refresh frame size
    self.FunctionFilter_ModifierPnl.update_width()

    ## update variable because the modifier now exists
    self.FUNCTIONFILTER_MOD_EXISTS = True


def translate_canvas_coords(self, x, y):
    x1 = x + self.Offset_X - self.dotSize / 2
    y1 = y + self.Offset_X - self.dotSize / 2
    x2 = x + self.Offset_X + self.dotSize / 2
    y2 = y + self.Offset_X + self.dotSize / 2
    return x1, y1, x2, y2


def sort_dots(self):
    import operator
    SortedPositions = {}
    for dot in self.Dots:
        SortedPositions[dot] = (self.FunctionFilter_Canvas.coords(dot)[0] + self.dotSize / 2,
                                self.FunctionFilter_Canvas.coords(dot)[1] + self.dotSize / 2)
    return sorted(SortedPositions.items(), key=operator.itemgetter(1))


def find_dot_coord(self, dot):
    coord = self.FunctionFilter_Canvas.coords(dot)
    return coord[0] + self.dotSize / 2, coord[1] + self.dotSize / 2


def new_dot(self, event=None):
    x = self.FunctionFilter_Canvas.canvasx(event.x) - self.Offset_X
    y = self.FunctionFilter_Canvas.canvasy(event.y) - self.Offset_Y

    if check_coords_bounds(self, x, y):
        # don't create a new dot if one exists with the same x
        for dot in self.Positions:
            if dot[1][0] - self.Offset_X == x:
                return

        dot = self.FunctionFilter_Canvas.create_oval(translate_canvas_coords(self, x, y),
                                                     activefill="grey40", fill="black")
        self.FunctionFilter_Canvas.tag_bind(dot, "<B1-Motion>", lambda event: onlyUpAndDown(self, dot, event))
        self.FunctionFilter_Canvas.tag_bind(dot, "<Button-3>", lambda event: remove_dot(self, dot, event))
        self.Dots.append(dot)
        self.org_pos.append((dot, (x, y + self.dotSize)))
        redraw_canvas(self)


def onlyUpAndDown(self, dot, event=None):
    if event:
        y = self.FunctionFilter_Canvas.canvasy(event.y) - self.Offset_Y
        if -1 < y < 257:
            coords = self.FunctionFilter_Canvas.coords(dot)
            self.FunctionFilter_Canvas.coords(dot, int(coords[0]), y + self.Offset_X - self.dotSize / 2,
                                  int(coords[2]), y + self.Offset_X + self.dotSize / 2)
            redraw_canvas(self)

def check_coords_bounds(self, x, y):
    #if (self.bBox[0] < x < self.bBox[2]) and (self.bBox[1] < y < self.bBox[3]):
    if (0 < x < 200) and (0 < y < 200):
        return True
    else:
        return False


def remove_dot(self, dot, event=None):
    if event:
        self.FunctionFilter_Canvas.delete(dot)
        self.Dots.remove(dot)
        redraw_canvas(self)


def redraw_canvas(self):
    self.Positions = sort_dots(self)
    for line in self.Lines:
        self.FunctionFilter_Canvas.delete(line)
    for idx, dot in enumerate(self.Positions):
        if idx + 1 < len(self.Positions):
            xy1 = find_dot_coord(self, self.Positions[idx][0])
            xy2 = find_dot_coord(self, self.Positions[idx + 1][0])
            line = self.FunctionFilter_Canvas.create_line(xy1[0], xy1[1], xy2[0], xy2[1],
                                                          splinesteps=16, smooth=True,
                                                          fill="black")
            self.Lines.append(line)


def reset_canvas(self):
    ## remove everything except the first two dots in self.Dots
    ## they were appended in order
    for dot in self.Dots[2:]:
        self.FunctionFilter_Canvas.delete(dot)
    del self.Dots[2:]
    
    ## remove all except the first and last dots
    del self.Positions[1:len(self.Positions)-1]

    ## set the dots back to the starting position
    self.FunctionFilter_Canvas.coords(self.StartDot, translate_canvas_coords(self, 0, 185))
    self.FunctionFilter_Canvas.coords(self.EndDot, translate_canvas_coords(self, 185, 0))
    redraw_canvas(self)

    ## update preview
    preview_function_filter(self)

        
def update_function(self):
    if self.brightnessFirstTime:
        self.org_pos = list(self.Positions)
        self.brightnessFirstTime = False
    for dot in self.Dots:
        coords = self.FunctionFilter_Canvas.coords(dot)
        y = None
        for pos in self.org_pos:
            if dot == pos[0]:
                y = pos[1][1] - self.Offset_Y 
        self.FunctionFilter_Canvas.coords(dot, int(coords[0]), y + self.Offset_X - self.dotSize / 2,
                            int(coords[2]), y + self.Offset_X + self.dotSize / 2)
        redraw_canvas(self)


def preview_function_filter(self):
    render_image_preview(self, self.data.image)
    self.data.previewimage = function_filter(self, self.data.previewimage, self.Positions)
    show_image_preview(self, self.data.previewimage)
    
        
def apply_function_filter(self):
    ## Apply the effect
    self.data.image = function_filter(self, self.data.image, self.Positions)

    ## Show image
    render_photoimage(self)

    ## Cache
    self.UndoQueue.cache_append(self.data.image)
    handle_cache(self, self.data.image)

    ## Destroy the modifier
    close_functionfilter_modifier(self)

    ## Update statusbar
    self.StatusBar_lbl.configure(text='Applied function filter modifier')

       
def close_functionfilter_modifier(self):
    ## destroy the modifier
    self.FunctionFilter_ModifierPnl.destroy()

    ## update variable because the modifier does not exist anymore
    self.FUNCTIONFILTER_MOD_EXISTS = False

