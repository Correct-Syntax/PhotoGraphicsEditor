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

import json
#from tkinter import *

class WidgetTheme(object):
    def __init__(self, path='theme.swifttheme'):
        self.path = path

    def load_theme(self, path='theme.swifttheme'):
        ## load the theme
        with open(path) as Theme:
            LoadedTheme = json.load(Theme)
            
        self.HIGHLIGHTCOLOR = LoadedTheme["highlightcolor"]
        self.BASECOLOR = LoadedTheme["basecolor"]



## future #############################
## import theme 
##
##
##
## Theme = theme.WidgetTheme()
## print(Theme.HIGHLIGHTCOLOR)
########################################
