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
from PIL import Image, ImageOps, ImageChops


from lib.SWIFT.tooltip import ToolTip
from lib.SWIFT.flatbutton import FlatButton


def docker_histogram_ui(self):
    ## create the docker
    self.Histogram_Docker = self.Docker_Panel.create_item(text='Histogram',
                                                          value='Histogram Docker',
                                                          icon="lib/datafiles/icons/interface/HistogramDocker.png")

    ## add the docker
    self.Docker_Panel.add_item(self.Histogram_Docker)

    ## create the histogram canvas
    Histogram_Frame = Frame(self.Histogram_Docker.interior, bd=1, relief=SOLID)
    Histogram_Frame.pack(fill=BOTH)
    
    self.Histogram_Canvas = Canvas(Histogram_Frame, width=200, height=200, bg="#969696",
                                   highlightthickness=0)
    self.Histogram_Canvas.pack()
    ToolTip(self.Histogram_Canvas, "Click to update histogram")

    self.Histogram_Canvas.bind("<Button-1>", lambda event: update_histogram(self))


def update_histogram(self):
    if self.data.image!= None:
        margin = 1
        im = self.data.image
        self.Histogram_Canvas.delete(ALL)

        R, G, B = im.histogram()[:256], im.histogram()[256:512], im.histogram()[512:768]

        ## coordinates start at the top left corner
        ## x, y (...-value in range(i), ...-value of the histogram)
        ##   |
        ##   |
        ## x, y (...-value in range(i), 250-size of canvas)
        for i in range(len(R)):
            PixelNum = R[i]
            self.Histogram_Canvas.create_line(i+margin, 200, i+margin, 200-PixelNum/100.0+1-margin, fill="red")

        for i in range(len(G)):
            PixelNum = G[i]
            self.Histogram_Canvas.create_line(i+margin, 200, i+margin, 200-PixelNum/100.0+1-margin, fill="green")

        for i in range(len(B)):
            PixelNum = B[i]
            self.Histogram_Canvas.create_line(i+margin, 200, i+margin, 200-PixelNum/100.0+1-margin, fill="blue")
