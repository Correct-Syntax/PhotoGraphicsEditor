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
from lib.core.render.renderer import render_photoimage, render_image_preview, show_image_preview
from lib.core.urcache.handler import handle_cache
from lib.core.interface.zoom_handler import handle_zooming


def modifier_crop_ui(self):
    ## Panel
    self.Crop_ModifierPnl = ModifierFrame(self.Main_Modifier_Panel,
                                          text="Crop", default=True,
                                          icon="lib/datafiles/icons/interface/CropModifier.png",
                                          closecommand=lambda:close_crop_modifier(self))
    self.Crop_ModifierPnl.pack(fill=X)

    ## Modifier Button Frame
    Modifier_ButtonFrame = Frame(self.Crop_ModifierPnl.interior, bg="#969696",
                                 bd=1, relief=GROOVE)
    Modifier_ButtonFrame.pack(padx=2, pady=4, side=TOP, fill=X)

    Apply_Button = FlatButton(Modifier_ButtonFrame, text=' Apply ', width=10,
                              command=lambda: apply_crop_image(self))
    Apply_Button.pack(padx=2, pady=2, side=LEFT)
    ToolTip(Apply_Button, "Apply crop modifier", wtype='FLATBUTTON')

    Refresh_Button = FlatButton(Modifier_ButtonFrame, text=' Refresh ', width=10, state=DISABLED)
    Refresh_Button.pack(padx=2, pady=2, side=RIGHT)

    ## label
    Crop_lbl1 = Label(self.Crop_ModifierPnl.interior,
                      text='Drag handles to adjust crop', bg="#969696")
    Crop_lbl1.pack()

    Crop_lbl1 = Label(self.Crop_ModifierPnl.interior,
                      text='Enter to crop', bg="#969696")
    Crop_lbl1.pack()

    Crop_lbl1 = Label(self.Crop_ModifierPnl.interior,
                      text='Esc to cancel crop', bg="#969696")
    Crop_lbl1.pack()

    ## Create the crop box
    x = self.data.width
    y = self.data.height

    self.canvas.create_rectangle(x/4, y/4, 3*x/4, 3*y/4,
                                 outline ='black', width=2, tag='crop_box')
    self.canvas.create_rectangle(x/4, y/4, x/4+20, y/4+20,
                                 outline ='black', width=2, tag='crop_topleft')
    self.canvas.create_rectangle(3*x/4, y/4, 3*x/4-20, y/4+20,
                                 outline ='black', width=2, tag='crop_topright')
    self.canvas.create_rectangle(x/4, 3*y/4, x/4+20, 3*y/4-20,
                                 outline ='black', width=2, tag='crop_bottomleft')
    self.canvas.create_rectangle(3*x/4, 3*y/4, 3*x/4-20, 3*y/4-20,
                                 outline ='black', width=2, tag='crop_bottomright')

    ## Bindings
    self.canvas.bind("<Button-1>", lambda event: start_crop(self, event))
    self.canvas.bind("<B1-Motion>", lambda event: adjust_cropbox(self, event))
    self.bind("<Return>", lambda event: apply_crop_image(self))
    self.bind("<Key-Escape>", lambda event: close_crop_modifier(self))

    ## Delete the crop box so that it can be updated
    self.canvas.delete('select')

    ## refresh frame size
    self.Crop_ModifierPnl.update_width()

    ## update variable because the modifier now exists
    self.CROP_MOD_EXISTS = True


def start_crop(self, event):
    ## coords
    H, L = self.winfo_screenheight(), self.winfo_screenwidth()
    if self.data.image.size[1] < H and self.data.image.size[0] < L:
        event.x = int(event.x+self.xscrollbar.get()[0]*(int(L*0.6)))
        event.y = int(event.y+self.yscrollbar.get()[0]*(int(H*0.6)))
    else:
        event.x = int(event.x+self.xscrollbar.get()[0]*self.data.image.size[0])
        event.y = int(event.y+self.yscrollbar.get()[0]*self.data.image.size[1])
        
    self.obj = self.canvas.find_closest(event.x, event.y, halo=10)
    self.tag = self.canvas.gettags(self.obj)
    if self.tag != ('crop_box', 'current') and self.tag != ('crop_box',):
        self.rogner_obj = self.obj


def adjust_cropbox(self, event):
    ## In order to have an acurate crop, the canvas cannot be zoomed
    ## during the crop-box adjustment, therefore we unbind the binding for zoom
    ## and re-bind it later after the crop is finished
    self.canvas.unbind("<MouseWheel>")
    
    ## coords
    H, L = self.winfo_screenheight(), self.winfo_screenwidth()
    if self.data.image.size[1] < H and self.data.image.size[0] < L:
        event.x = int(event.x+self.xscrollbar.get()[0]*(int(L*0.6)))
        event.y = int(event.y+self.yscrollbar.get()[0]*(int(H*0.6)))
    else:
        event.x = int(event.x+self.xscrollbar.get()[0]*self.data.image.size[0])
        event.y = int(event.y+self.yscrollbar.get()[0]*self.data.image.size[1])
        
    try: 
        self.canvas.coords(self.rogner_obj, event.x-10, event.y-10, event.x+10, event.y+10)
        self.obj = self.canvas.gettags(self.rogner_obj)
        
        if self.obj == ('crop_topleft',) or self.obj == ('crop_topleft','current'):
            x1, y1, x2, y2 = self.canvas.coords('crop_bottomright')
            self.canvas.coords('crop_box', event.x-10, event.y-10, x2, y2)
            self.canvas.coords('crop_bottomleft', event.x-10, y1, event.x+10, y2)
            self.canvas.coords('crop_topright', x1, event.y-10, x2, event.y+10)
            
        elif self.obj == ('crop_topright',) or self.obj == ('crop_topright', 'current'):
            x1, y1, x2, y2 = self.canvas.coords('crop_bottomleft')
            self.canvas.coords('crop_box', x1, event.y-10, event.x+10, y2)
            self.canvas.coords('crop_topleft', x1, event.y-10, x2, event.y+10)
            self.canvas.coords('crop_bottomright', event.x-10, y1, event.x+10, y2)
        
        elif self.obj == ('crop_bottomleft',) or self.obj == ('crop_bottomleft','current'):
            x1, y1, x2, y2 = self.canvas.coords('crop_topright')
            self.canvas.coords('crop_box', event.x-10, y1, x2, event.y+10)
            self.canvas.coords('crop_topleft', event.x-10, y1, event.x+10, y2)
            self.canvas.coords('crop_bottomright', x1, event.y-10, x2, event.y+10)
            
        elif self.obj == ('crop_bottomright',) or self.obj == ('crop_bottomright', 'current'):
            x1, y1, x2, y2 = self.canvas.coords('crop_topleft')
            self.canvas.coords('crop_box', x1,y1, event.x+10, event.y+10)
            self.canvas.coords('crop_bottomleft', x1, event.y-10, x2, event.y+10)
            self.canvas.coords('crop_topright', event.x-10, y1, event.x+10, y2)

    except:
        pass


def apply_crop_image(self):
    ## Setup the coords
    x1, y1, x2, y2 = self.canvas.coords('crop_box')

    ## crop the image
    self.data.image = self.data.image.crop((int(x1/self.zoom_value),
                                            int(y1/self.zoom_value),
                                            int(x2/self.zoom_value),
                                            int(y2/self.zoom_value)))

    ## Show image
    render_photoimage(self)

    ## Cache
    self.UndoQueue.cache_append(self.data.image)
    handle_cache(self, self.data.image)

    ## Clear up canvas data
    self.canvas.delete('crop_box')
    self.canvas.delete('crop_topleft')
    self.canvas.delete('crop_topright')
    self.canvas.delete('crop_bottomleft')
    self.canvas.delete('crop_bottomright')

    ## Unbind bindings
    self.canvas.unbind("<Button-1>")
    self.canvas.unbind("<B1-Motion>")
    self.unbind("<Return>")
    self.unbind("<Key-Escape>")

    ## Rebind binding for zoom
    self.canvas.bind("<MouseWheel>", lambda event: handle_zooming(self, event))

    ## Destroy the modifier
    close_crop_modifier(self)

    ## Update statusbar
    self.StatusBar_lbl.configure(text='Applied crop modifier')


def close_crop_modifier(self):
    ## Clear up canvas data
    self.canvas.delete('crop_box')
    self.canvas.delete('crop_topleft')
    self.canvas.delete('crop_topright')
    self.canvas.delete('crop_bottomleft')
    self.canvas.delete('crop_bottomright')

    ## Unbind bindings
    self.canvas.unbind("<Button-1>")
    self.canvas.unbind("<B1-Motion>")
    self.unbind("<Return>")
    self.unbind("<Key-Escape>")

    ## Rebind binding for zoom
    self.canvas.bind("<MouseWheel>", lambda event: handle_zooming(self, event))

    ## destroy the modifier
    self.Crop_ModifierPnl.destroy()

    ## update variable because the modifier does not exist anymore
    self.CROP_MOD_EXISTS = False  
