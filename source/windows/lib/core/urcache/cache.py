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
from collections import *
from tkinter import *
from tkinter.constants import *
from tkinter import ttk

from lib.core.render.renderer import render_photoimage


class Cache(deque):
    """ A thin wrapper around deque. """
    def __init__(self):

        ## Get the allowed size of the deques
        self.sz = int(open("lib/datafiles/cfg/DEQUES_MAXSIZE.cfg").read())

        ## Create the deque
        deque.__init__(self, iterable=[], maxlen=self.sz)


    def cache_append(self, img):
        """ Appends images into the cache. """
        self.append(img.copy())

    def cache_maxsize(self):
        """ Gets the maximum size of the cache. """
        return self.sz

    
    def cache_size(self):
        """ Gets the current size of the cache. """
        return len(self)


    def cache_isfull(self):
        """ Checks whether the cache is full. """
        return len(self) == self.sz


    def cache_isempty(self):
        """ Checks whether the cache is empty. """
        return len(self) == 1
    

def undo_action(self):
    """ We use deques to make the Undo and Redo efficient and avoid memory issues.
    After each change, we append the new version of the image to the Undo queue."""
    if len(self.UndoQueue) > 0:        
        # The last element of the Undo Deque is the current
        # version of the image
        lastqueue_img = self.UndoQueue.pop()
        
        # we want the current version when the user presses redo after undo
        self.RedoQueue.appendleft(lastqueue_img)
        
    # get the previous version of the image
    if len(self.UndoQueue) > 0:
        self.data.image = self.UndoQueue[-1]

    ## Cache
    try:
        active = self.Cache_Listbox.curselection()
        self.Cache_Listbox.selection_clear(0, self.UndoQueue.cache_maxsize())

        if active[0] < 0:
            pass
        else:
            self.Cache_Listbox.selection_set(active[0] - 1)
    except:
        pass
    
    ## Show image
    render_photoimage(self)
        
    ## Update statusbar
    self.StatusBar_lbl.configure(text='Undo was successful')


def redo_action(self):
    """ Redo the action that was undone. """
    if len(self.RedoQueue) > 0:
        
        # get the image redo
        self.data.image = self.RedoQueue[0]
        
    if len(self.RedoQueue) > 0:
        lastqueue_img = self.RedoQueue.popleft()
        self.UndoQueue.cache_append(lastqueue_img)

    ## Cache
    try:
        active = self.Cache_Listbox.curselection()
        self.Cache_Listbox.selection_clear(0, self.UndoQueue.cache_maxsize())

        if active[0] < 0:
            pass
        else:
            self.Cache_Listbox.selection_set(active[0] + 1)
    except:
        pass
        
    ## Show image
    render_photoimage(self)
        
    ## Update statusbar
    self.StatusBar_lbl.configure(text='Redo was successful')


def reset_actions(self):
    """ To reset the image, we clear the undo and redo deques and get the original
    image.  Clears self.data.image and both deques. """
    if self.data.image!= None:
        
        ## Revert back to the original image
        self.data.image = self.OriginalImageCopy.copy()

        ## Clear the undo and redo deques
        self.UndoQueue.clear()
        self.RedoQueue.clear()

        ## Delete all of the labels
        self.Cache_Listbox.delete(1, END)

        ## Show image
        render_photoimage(self)
        
        ## Update statusbar
        self.StatusBar_lbl.configure(text='Successfully reset image')


def clear_cache(self):
    """ An option to clear the cache. Useful for when memory issues happen. """
    ## Clear the undo and redo deques
    self.UndoQueue.clear()
    self.RedoQueue.clear()

    ## Re-create the undo and redo deques
    self.UndoQueue = Cache()
    self.RedoQueue = Cache()

    ## Delete all of the labels
    self.Cache_Listbox.delete(1, END)
    
    ## Update statusbar
    self.StatusBar_lbl.configure(text='Successfully cleared undo/redo cache')
