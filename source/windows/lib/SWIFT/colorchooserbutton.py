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


class ColorChooserButton(Label):
    ## A thin wrapper around the Label widget, so that we do not have to specify
    ## the default variables for the colorchooser button every time we use it.
    def __init__(self, master, command=None, **kwargs):
        Label.__init__(self, master, bg='#FFFFFF', fg='black', relief=SOLID,
                       bd=1, text='#FFFFFF', font=("Calibri", 10))
