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

from lib.core.optypes.modifier.layer_image_ui import modifier_layerimage_ui
from lib.core.optypes.modifier.function_filter_ui import modifier_functionfilter_ui
from lib.core.optypes.modifier.crop_ui import modifier_crop_ui
from lib.core.optypes.modifier.add_text_ui import modifier_addtext_ui

def validate_modifier(self, modifiername):
    if self.data.image != None:
        if modifiername == 'Layer Image':
            if self.LAYERIMAGE_MOD_EXISTS == False:
                modifier_layerimage_ui(self)

        if modifiername == 'Function Filter':
            if self.FUNCTIONFILTER_MOD_EXISTS == False:
                modifier_functionfilter_ui(self)

        if modifiername == 'Crop':
            if self.CROP_MOD_EXISTS == False:
                modifier_crop_ui(self)

        if modifiername == 'Add Text':
            if self.ADDTEXT_MOD_EXISTS == False:
                modifier_addtext_ui(self)


