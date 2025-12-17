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

import os
from tkinter import *
from tkinter.constants import *
from tkinter import ttk

def update_imageinfo(self):
    """ Update the image info property. """
    if self.data.image!= None:
        self.ImageInfo_ImageName_Lbl.configure(text=self.OriginalImFilePath)
        self.ImageInfo_ImageSize_Lbl.configure(text='{}x{}'.format(self.data.image.size[0],
                                                                   self.data.image.size[1]))
        self.ImageInfo_ImageMode_Lbl.configure(text=self.data.image.mode)
        try:
            self.ImageInfo_ImageFileSize_Lbl.configure(text=str(os.path.getsize(self.OriginalImFilePath)/1000) + 'kB')

        except:
            filesize = ''
