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
from lib.core.edit.layer_image import layer_image


def modifier_layerimage_ui(self):
    ## Panel
    self.LayerImage_ModifierPnl = ModifierFrame(self.Main_Modifier_Panel,
                                                text="Layer Image", default=True,
                                                icon="lib/datafiles/icons/interface/LayerImageModifier.png",
                                                closecommand=lambda:close_layerimage_modifier(self))
    self.LayerImage_ModifierPnl.pack(fill=X)

    ## Modifier Button Frame
    Modifier_ButtonFrame = Frame(self.LayerImage_ModifierPnl.interior, bg="#969696",
                                 bd=1, relief=GROOVE)
    Modifier_ButtonFrame.pack(padx=2, pady=4, side=TOP, fill=X)

    Apply_Button = FlatButton(Modifier_ButtonFrame, text=' Apply ', width=10,
                              command=lambda: apply_layer_image(self))
    Apply_Button.pack(padx=2, pady=2, side=LEFT)
    ToolTip(Apply_Button, "Apply layer image modifier", wtype='FLATBUTTON')

    Refresh_Button = FlatButton(Modifier_ButtonFrame, text=' Refresh ', width=10, 
                              command=lambda: preview_layer_image(self))
    Refresh_Button.pack(padx=2, pady=2, side=RIGHT)
    ToolTip(Refresh_Button, "Refresh preview of layer image modifier", wtype='FLATBUTTON')

    ## Layer Image 
    LayerImage_Frame = Frame(self.LayerImage_ModifierPnl.interior, bg="#969696")
    LayerImage_Frame.pack(fill=X)

    self.OpenLayerImage_Button = FlatButton(LayerImage_Frame, text=' Open Image ',
                                            command=lambda: open_layer_image(self))
    self.OpenLayerImage_Button.pack(padx=2, pady=2, side=LEFT)
    ToolTip(self.OpenLayerImage_Button, "Open image to layer", wtype='FLATBUTTON')
    
    self.LayerImageBlendMode_Dropdown = DropDownButton(LayerImage_Frame, text='Add')
    self.LayerImageBlendMode_Dropdown.pack(padx=2, pady=2, side=RIGHT)
    DropDownMenu(self.LayerImageBlendMode_Dropdown, chars=90,
                 options=[
                     'Add',
                     'Add Mod',
                     'Subtract',
                     'Subtract Mod',
                     'Multiply',
                     'Screen',
                     'Difference',
                     'Darker',
                     'Lighter'
                     ],
                 commands={
                     'Add': lambda:preview_layer_image(self),
                     'Add Mod': lambda:preview_layer_image(self),
                     'Subtract': lambda:preview_layer_image(self),
                     'Subtract Mod': lambda:preview_layer_image(self),
                     'Multiply': lambda:preview_layer_image(self),
                     'Screen': lambda:preview_layer_image(self),
                     'Difference': lambda:preview_layer_image(self),
                     'Darker': lambda:preview_layer_image(self),
                     'Lighter': lambda:preview_layer_image(self)
                     },
                 flagtext="Blend Mode")

    ## Checkbutton
    self.UseLayerImageFromImageLib_Var = IntVar()
    self.UseLayerImageFromImageLib_Var.set(0)
    UseLayerImageFromImageLib_Checkbutton = Checkbutton(self.LayerImage_ModifierPnl.interior,
                                                        text='Use Image From Library',
                                                        bg="#969696", selectcolor="#94afc9",
                                                        activebackground="#969696",
                                                        variable=self.UseLayerImageFromImageLib_Var,
                                                        command=lambda: use_image_library_layer_image(self))
    UseLayerImageFromImageLib_Checkbutton.pack(padx=2, pady=2, anchor=W)
    ToolTip(UseLayerImageFromImageLib_Checkbutton, "Use the currently selected image in the Image Library as the layer image")
    
    self.LayerImage_ModifierPnl.update_width()

    ## update variable because the modifier now exists
    self.LAYERIMAGE_MOD_EXISTS = True


def use_image_library_layer_image(self):
    if self.UseLayerImageFromImageLib_Var.get() == 0:
        ## enable the open image button
        self.OpenLayerImage_Button.configure(state=NORMAL)
        
    if self.UseLayerImageFromImageLib_Var.get() == 1:
        ## disable the open image button
        self.OpenLayerImage_Button.configure(state=DISABLED)

        ## use the currently selected image from the Image Library
        self.OpenedLayerImage = Image.open(self.data.selectedimagefromlib)

        ## preview
        preview_layer_image(self)

def preview_layer_image(self):
    try:
        render_image_preview(self, self.data.image)
        self.data.previewimage = layer_image(self, self.data.previewimage,
                                             self.OpenedLayerImage.copy(),
                                             self.LayerImageBlendMode_Dropdown.cget("text"))
        show_image_preview(self, self.data.previewimage)

    except AttributeError:
        self.StatusBar_lbl.configure(text='Please open an image to layer!')

def open_layer_image(self):
    ## Dialog
    Dialog = OpenFileDialog(self, title='Open Image To Layer...',
                            filetypes=['.jpg', '.jpeg', '.bmp', '.png', '.tiff', '.tif'])
    self.OpenedLayerImage = Image.open(Dialog.go())
    preview_layer_image(self)

    
def apply_layer_image(self):
    try:
        ## Apply layer image effect
        self.data.image = layer_image(self, self.data.image, self.OpenedLayerImage,
                                      self.LayerImageBlendMode_Dropdown.cget("text"))

        ## Show image
        render_photoimage(self)

        ## Cache
        self.UndoQueue.cache_append(self.data.image)
        handle_cache(self, self.data.image)

        ## Destroy the modifier
        close_layerimage_modifier(self)

        ## Update statusbar
        self.StatusBar_lbl.configure(text='Applied layer image modifier')

    ## If there is no image to layer, update statusbar
    except AttributeError:
        self.StatusBar_lbl.configure(text='Please open an image to layer before applying the modifier!')
        

def close_layerimage_modifier(self):
    ## destroy the modifier
    self.LayerImage_ModifierPnl.destroy()

    ## update variable because the modifier does not exist anymore
    self.LAYERIMAGE_MOD_EXISTS = False
