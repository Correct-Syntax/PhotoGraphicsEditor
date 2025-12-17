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

from lib.SWIFT.tooltip import ToolTip
from lib.SWIFT.flatbutton import FlatButton


def docker_preview_ui(self):
    ## create the docker
    self.Preview_Docker = self.Docker_Panel.create_item(text='Preview',
                                                        value='Preview Docker',
                                                        icon="lib/datafiles/icons/interface/PreviewDocker.png")

    ## add the docker
    self.Docker_Panel.add_item(self.Preview_Docker)

    ## create the preview canvas
    ImagePreview_Frame = Frame(self.Preview_Docker.interior, bd=1, relief=SOLID)
    ImagePreview_Frame.pack()

    self.ImagePreview_Canvas = Canvas(ImagePreview_Frame, width=200, bg="#969696",
                                      highlightthickness=0, height=200)
    self.ImagePreview_Canvas.pack()
