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

from lib.SWIFT.dragdropdockerlist import DragDropDockerList, DockerFrame
from lib.core.optypes.docker.preview_ui import docker_preview_ui
from lib.core.optypes.docker.image_library_ui import docker_image_library_ui
from lib.core.optypes.docker.histogram_ui import docker_histogram_ui


def left_sidebar_ui(self):
    ## Docker panel
    self.BaseDocker_Panel = Frame(self, bg="grey80", bd=1, relief=SOLID)
    self.BaseDocker_Panel.pack(fill=BOTH, side=RIGHT)

    self.DockerPanelCanvas = Canvas(self.BaseDocker_Panel, highlightthickness=0,
                                    width=220, height=1200, bg="#969696")
    self.Docker_Panel = DragDropDockerList(self.BaseDocker_Panel, 200, 260,
                                           offset_x=10, offset_y=10, gap=10,
                                           item_borderwidth=1, item_relief=SOLID)
    self.Docker_Panel.pack(expand=True, fill=BOTH)
    DockerPanelScrollbar = Scrollbar(self.BaseDocker_Panel, orient=VERTICAL,
                                     command=self.DockerPanelCanvas.yview)
    self.DockerPanelCanvas.configure(yscrollcommand=DockerPanelScrollbar.set)
    DockerPanelScrollbar.pack(side=LEFT, fill=Y)
    self.DockerPanelCanvas.pack(side=RIGHT, fill=BOTH, expand=True)

    ## add the dockers
    docker_preview_ui(self)
    docker_image_library_ui(self)
    docker_histogram_ui(self)
    
    self.DockerPanelCanvas.create_window((0, 0), window=self.Docker_Panel, anchor=N)

    self.Docker_Panel.bind("<Configure>", lambda event: config_dockerframe(self))

def config_dockerframe(self):
    self.DockerPanelCanvas.configure(scrollregion=self.DockerPanelCanvas.bbox("all"))
