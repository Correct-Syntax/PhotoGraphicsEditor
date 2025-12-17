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
import imghdr
from pathlib import Path
from tkinter import *
from tkinter.constants import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageGrab

from lib.SWIFT.openfiledialog import OpenFileDialog
from lib.core.render.renderer import render_photoimage
from lib.core.optypes.docker.histogram_ui import update_histogram
from lib.core.optypes.property.file.file_output import save_file_as
from lib.core.urcache.handler import handle_cache


def open_file(self):
    """ Open an image into the editor. """

    ## If there is an image loaded already
    if self.data.image != None:
        a = messagebox.askyesno('Save Edited File?', '''
If you do not save the file, any change(s) to
the current image will be lost!
        
Would you like to save the current image before
opening a new one?
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

    ## Dialog
    Dialog = OpenFileDialog(self, title='Open File...',
                            filetypes=['.jpg', '.jpeg', '.bmp', '.png', '.tiff', '.tif'])
    ImageName = Dialog.go()

    ## Find out what the filetype is
    try:
        Filetype  = ""
        Filetype = imghdr.what(ImageName)

    except AttributeError:
        pass

    if Filetype in ['jpg', 'jpeg', 'bmp', 'png', 'tiff', 'tif']:
        try:
            ## Open image
            OpenedImName = Image.open(ImageName)
            self.data.image = OpenedImName.copy()

            ## Get copies of the image for reset function
            self.OriginalImageCopy = OpenedImName.copy()

            ## Cache
            self.Cache_Listbox.delete(0)
            self.Cache_Listbox.insert(0, '<original image>')
            self.Cache_Listbox.configure(height=self.UndoQueue.cache_maxsize())
            self.UndoQueue.cache_append(OpenedImName)
            handle_cache(self, OpenedImName)

            ## Get image properties
            self.OriginalImFilePath = ImageName

            ## Assign it as a recent file
    ##            RECENT_FILE = open('lib\\data\\RECENT_FILES.cfg','w')
    ##            RECENT_FILE.write(ImageName)
    ##            RECENT_FILE.close()
            
            ## Show image
            render_photoimage(self)

            ## set the mode value to be whatever the image mode is
            self.ImageMode_Var.set(self.data.image.mode)

            ## update the histogram docker
            update_histogram(self)

            ## Update statusbar
            self.StatusBar_lbl.configure(text='{}  {}x{}  {}'.format(self.OriginalImFilePath,
                                                                     self.data.image.size[0],
                                                                     self.data.image.size[1],
                                                                     self.data.image.mode))

        # otherwise show an error
        except OSError:
            messagebox.showerror('Unable To Open File!', '''
The selected file appears to be corrupted!
''')

        except AttributeError:
            messagebox.showerror('Unable To Open File!', '''
The selected file appears to be corrupted or missing!
''')

    else:
        # if a file is not opened, pass
        if Filetype == '':
            pass

        else:
            messagebox.showerror('Cannot Open File!', '''
You have selected a file with an unsupported format!
''')


def open_from_clipboard(self):
    """ Open an image from the clipboard. """

    ## If there is an image loaded already
    if self.data.image != None:
        a = messagebox.askyesno('Save Edited File?', '''
If you do not save the file, any change(s) to
the current image will be lost!
        
Would you like to save the current image before
opening a new one?
''', icon='warning')

        if a == True:
            pass
            ## Save the image
            save_file_as(self)

    try:
        ## Get the image from clipboard, if there is one
        ClipboardImgName = ImageGrab.grabclipboard()

        ## Create Image
        self.data.image = ClipboardImgName.copy()

        ## Clear the undo and redo deques
        self.UndoQueue.clear()
        self.RedoQueue.clear()

        ## Clear the cache
        self.Cache_Listbox.delete(0, END)
        
        ## Cache
        self.Cache_Listbox.delete(0)
        self.Cache_Listbox.insert(0, '<original image>')
        self.Cache_Listbox.configure(height=self.UndoQueue.cache_maxsize())
        self.UndoQueue.cache_append(ClipboardImgName)
        handle_cache(self, ClipboardImgName)

        # Set image file path to be none since the image is only in the
        # memory and there is no real path to the image!
        self.OriginalImFilePath = ('')
        
        ## Show image
        render_photoimage(self)

        ## set the mode value to be whatever the image mode is
        self.ImageMode_Var.set(self.data.image.mode)

        ## update the histogram docker
        update_histogram(self)

        ## Update statusbar
        self.StatusBar_lbl.configure(text='Created image from clipboard:  {}x{}  {}'.format(self.data.image.size[0],
                                                                                            self.data.image.size[1],
                                                                                            self.data.image.mode))
    except:
        messagebox.showerror('Empty Clipboard!', '''
Cannot create image from empty clipboard!
''')

