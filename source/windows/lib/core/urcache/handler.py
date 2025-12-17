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


def handle_cache(self, img):
    """ Handles the cache operations.
    ================================
    img - the image to be copied to UndoQueue stack. Most of the time, this will
    be 'self.data.image'.
    """
    if self.UndoQueue.cache_size() == self.UndoQueue.cache_maxsize():
        self.Cache_Listbox.delete(1)

    self.Cache_Listbox.insert(self.UndoQueue.cache_size() + 1, img)
    self.Cache_Listbox.selection_clear(0, self.UndoQueue.cache_maxsize())
    self.Cache_Listbox.selection_set(self.UndoQueue.cache_size())
