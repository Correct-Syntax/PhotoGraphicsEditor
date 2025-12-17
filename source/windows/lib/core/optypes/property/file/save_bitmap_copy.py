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
import copy
from tkinter import *
from tkinter.constants import *
from tkinter import messagebox
from PIL import Image

from lib.SWIFT.savefiledialog import SaveFileDialog


def save_bitmap_copy(self):
    if self.data.image!= None:
        try:
            ## Resize the image to half the resolution
            im = self.data.image.copy()
            w, h = im.size
            im = im.resize((int(w/2), int(h/2)))

            ## Get the name of the user
            username = os.getlogin()

            ## Define the number of the image
            directory = os.listdir('C:\\Users\\{}\\Pictures'.format(username))
            num = -1
            for file in directory:
                num = num + 1

            ## Save the bmp
            im.save('C:\\Users\\{}\\Pictures\\bmpcopy_{}.bmp'.format(username, str(num)))

            ## Update status bar
            self.StatusBar_lbl.configure(text='Bitmap was saved successfully as: C:/Users/{}/Pictures/bmpcopy_{}.bmp'.format(username, str(num))) 

        except:
            answer = messagebox.askyesno('Error!', '''
            There was an error saving the bitmap copy

            Would you like to save the image manually?''', icon='error')
            
            if answer == True:
                AcceptedFileType = [('BMP Image', '*.bmp')]

                ## Save bitmap
                Dialog = SaveFileDialog(self, title='Save Bitmap Copy...',
                                        initialfile='untitled.bmp',
                                        filetypes=['.bmp'])
                bmp_filename = Dialog.go()
                
                im.save(bmp_filename)

                ## Update status bar
                self.StatusBar_lbl.configure(text='Bitmap was saved successfully as: {}'.format(bmp_filename))      


