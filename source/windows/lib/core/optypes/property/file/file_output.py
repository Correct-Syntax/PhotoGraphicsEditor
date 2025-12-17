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
from tkinter import ttk, messagebox
from PIL import Image

from lib.SWIFT.savefiledialog import SaveFileDialog
from lib.core.render.renderer import render_photoimage


def save_file(self):
    """ Save the current image back to the original image's path.
    WARNING: OVERWRITES THE ORIGINAL IMAGE!! """
    if self.data.image!= None:
        ## If the image is an actual opened image
        if self.OriginalImFilePath != '':
            self.data.image.save(self.OriginalImFilePath)

            ## Update statusbar
            self.StatusBar_lbl.configure(text='File was saved over: {}'.format(self.OriginalImFilePath))

        ## If the image was created with this program
        else:
            answer = messagebox.askyesno('File needs to be saved!', '''
            This file needs to be saved as an image!

            Would you like to save it as an image now?''')
            
            if answer == True:
                ## Save image
                save_file_as(self)

                ## Get filepath
                self.OriginalImFilePath = self.filename


def save_file_as(self):
    """ Saves the current image as a separate file. """
    if self.data.image!= None:
        try:
            ## Ask where the user wants to save the file
            Dialog = SaveFileDialog(self, title='Save File As...', initialfile='untitled.png',
                                    filetypes=['.jpg', '.jpeg', '.bmp', '.png',
                                               '.tiff', '.tif', '.ico', '.jpe',
                                               '.ppm', '.pcx', '.gif', '.ps'])

            self.filename = Dialog.go()

            ## Find out what the filetype is
            filetype = os.path.splitext(self.filename)[1]

            if filetype in ['.jpg', '.jpeg', '.bmp', '.png', '.tiff', '.tif',
                            '.ico', '.jpe', '.ppm', '.pcx', '.gif', '.ps']:

                ## If the file extension is .ps
                if filetype == '.ps':
                    save_file_as_postscript(self)

                else:
                    ## Save image as filename
                    im = self.data.image
                    im.save(self.filename)

                    ## Update statusbar
                    self.StatusBar_lbl.configure(text='File was saved as: {}'.format(self.filename))
            else:
                messagebox.showerror('Error Saving File!', '''
                - You have not saved the file

                - You attempted to save the file as
                an unsupported format''')   

        except ValueError:
            messagebox.showerror('Error Saving File!', '''
            There was an error saving the file!
            
            Please convert the file to RGB before
            saving it as .pcx''')  


def save_file_as_postscript(self):
    ## Update everything
    self.update_idletasks()

    ## Save image as a postscript
    self.canvas.postscript(x=0, y=0, colormode='color', file=self.filename)

    ## Update statusbar
    self.StatusBar_lbl.configure(text='Image saved as: {}'.format(self.filename))
   
