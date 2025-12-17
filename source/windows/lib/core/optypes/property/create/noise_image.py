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
from tkinter import ttk
from PIL import Image

from lib.core.render.renderer import render_photoimage
from lib.core.optypes.property.file.file_output import save_file_as
from lib.core.urcache.handler import handle_cache

from lib.core.optypes.property.create.algorithms.truecolor_plasma_noise import create_truecolorplasma_noise
from lib.core.optypes.property.create.algorithms.perlin_noise import create_perlincloud_noise, create_perlinmarble_noise, create_perlinwood_noise

        
def create_noise_image(self):
    ## If there is an image loaded already
    if self.data.image != None:
        a = messagebox.askyesno('Save Edited File?', '''
If you do not save the file, any change(s) to
the current image will be lost!
        
Would you like to save the current image before
creating a new one?
''', icon='warning')

        if a == True:
            pass
            ## Save the image
            save_file_as(self)

        ## Clear the undo and redo deques
        self.UndoQueue.clear()
        self.RedoQueue.clear()

        ## Clear the cache
        self.Cache_Listbox.delete(0, END)

    if self.NoiseType_Dropdown.cget("text") == 'Truecolor Plasma':
        self.data.image = create_truecolorplasma_noise(self, get_noiseimage_dimensions(self))

    if self.NoiseType_Dropdown.cget("text") == 'Perlin (Cloud)':
        self.data.image = create_perlincloud_noise(self, get_noiseimage_dimensions(self))

    if self.NoiseType_Dropdown.cget("text") == 'Perlin (Marble)':
        self.data.image = create_perlinmarble_noise(self, get_noiseimage_dimensions(self))

    if self.NoiseType_Dropdown.cget("text") == 'Perlin (Wood)':
        self.data.image = create_perlinwood_noise(self, get_noiseimage_dimensions(self))


    ## Get copies of the image for reset function
    self.OriginalImageCopy = self.data.image.copy()
    
    ## Cache
    self.Cache_Listbox.delete(0)
    self.Cache_Listbox.insert(0, '<original image>')
    self.Cache_Listbox.configure(height=self.UndoQueue.cache_maxsize())
    self.UndoQueue.cache_append(self.data.image)
    handle_cache(self, self.data.image)

    # Set image file path to be none since the image is only in the
    # memory and there is no real path to the image!
    self.OriginalImFilePath = ('')
    
    ## Show image
    render_photoimage(self)

    ## Update statusbar
    self.StatusBar_lbl.configure(text='Created {} type noise image:  {}x{}  {}'.format(self.NoiseType_Dropdown.cget("text"),
                                                                                       self.data.image.size[0],
                                                                                       self.data.image.size[1],
                                                                                       self.data.image.mode))


def get_noiseimage_dimensions(self):
    if self.NoiseImageSize_Dropdown.cget("text") == 'Icon 16x16':
        return 16, 16

    if self.NoiseImageSize_Dropdown.cget("text") == '520x520':
        return 520, 520

    if self.NoiseImageSize_Dropdown.cget("text") == '1024x1024':
        return 1024, 1024

    if self.NoiseImageSize_Dropdown.cget("text") == 'PAL 720x576':
        return 720, 576

    if self.NoiseImageSize_Dropdown.cget("text") == 'NTSC 720x486':
        return 720, 486
