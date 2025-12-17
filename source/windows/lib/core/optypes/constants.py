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


def types_constants(self):
    """ Constants for whether a type (property or modifier) exists
    at any given time in the sidebar. "Property" type panels should exist all
    the time, but there may be a use for these constants in some other way. """
    ## Property
    self.IMAGEINPUT_PROP_EXISTS = True
    self.IMAGEOUTPUT_PROP_EXISTS = True
    self.IMAGEINFO_PROP_EXISTS = True
    self.UNDOREDORESET_PROP_EXISTS = True
    self.TRANSFORMIMAGE_PROP_EXISTS = True
    self.IMAGEMODE_PROP_EXISTS = True
    self.VIEW_PROP_EXISTS = True
    self.CACHE_PROP_EXISTS = True
    
    self.GENERATENORMALMAP_PROP_EXISTS = True
    self.ZOOM_PROP_EXISTS = True
    self.USERPREFERENCES_PROP_EXISTS = True

    
    ## Modifier
    self.CROP_MOD_EXISTS = False
    self.LAYERIMAGE_MOD_EXISTS = False
    self.FUNCTIONFILTER_MOD_EXISTS = False
    self.ADDTEXT_MOD_EXISTS = False
    
    self.ADDDROPSHADOW_MOD_EXISTS = False
    self.RESIZEIMAGE_MOD_EXISTS = False
    self.ADDREMOVEBORDER_MOD_EXISTS = False
    self.ENHANCEIMAGE_MOD_EXISTS = False


