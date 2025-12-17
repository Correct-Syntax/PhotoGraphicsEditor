#! python3
## PhotoGraphics Editor copyright © 2019 Noah Rahm. All rights reserved.
##
## This program is free software: you can redistribute it and/or modify it 
## under the terms of the PhotoGraphics Editor Project License.
##
## PHOTOGRAPHICS EDITOR IS PROVIDED `AS IS' WITHOUT  WARRANTY OF ANY
## KIND, EITHER  EXPRESS OR IMPLIED,  INCLUDING, BUT NOT  LIMITED TO,
## WARRANTIES  OF  MERCHANTABILITY   AND  FITNESS  FOR  A  PARTICULAR
## PURPOSE.  IN NO EVENT WILL ANY OF THE AUTHORS OR COPYRIGHT HOLDERS
## BE LIABLE  FOR ANY DAMAGES CAUSED  BY THE USE OR THE INABILITY TO
## USE PHOTOGRAPHICS EDITOR.
##
## Contributor(s): Noah Rahm

import os
from tkinter import *

from lib.core.urcache.cache import Cache
from lib.core.interface.topbar import topbar_ui
from lib.core.interface.statusbar import statusbar_ui
from lib.core.interface.canvas import canvas_ui
from lib.core.interface.rightsidebar import right_sidebar_ui
from lib.core.interface.leftsidebar import left_sidebar_ui
from lib.core.interface.splashscreen import splashscreen_ui
from lib.core.window.bindings_handler import wm_bindings_handler
from lib.core.window.quit import quit_program
from lib.core.optypes.property.default import types_default
from lib.core.optypes.constants import types_constants
from lib.datafiles.icons.interface.icon_handler import interface_icon_loader
from lib.pluginloader.loader import load_plugins

__version__ = "1.1.0"
__author__ = "Noah Rahm"

    
class Main_Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('PhotoGraphics Editor')
        self.wm_iconbitmap('lib/datafiles/icons/program/Program_Icon.ico')
        x = self.winfo_screenwidth()-1630
        y = self.winfo_screenheight()-828
        self.geometry("1630x828+%d+%d" % (x/2, y/2))
        self.minsize(750, 428)
        self.maxsize(1630, 828)
        self.configure(bg="grey40")

        ## Setup canvas data
        class Structure:
            pass
        self.data = Structure()
        self.data.width = 1100
        self.data.height = 740

        ## setup image data
        self.data.image = None
        self.data.previewimage = None
        self.data.selectedimagefromlib = "lib/datafiles/imglib/img_001.png"
        self.zoom_image = None
        self.zoom_value = 1.0
        
        ## Setup undo and redo deques
        self.UndoQueue = Cache()
        self.RedoQueue = Cache()

        ## Load icons
        interface_icon_loader(self)

        ## Build the GUI
        topbar_ui(self)
        #splashscreen_ui(self)
        statusbar_ui(self)
        right_sidebar_ui(self)
        canvas_ui(self)
        left_sidebar_ui(self)
    
        ## Load default property panels
        types_default(self)
        
        ## Load plugins
        load_plugins(self)

        ## Keyboard shortcuts
        wm_bindings_handler(self)

        ## Constants for types
        types_constants(self)
        
        ## Prompt quit on exit
        #self.protocol("WM_DELETE_WINDOW", lambda: quit_program(self))


if __name__ == '__main__':
    App = Main_Application()
    App.mainloop()
