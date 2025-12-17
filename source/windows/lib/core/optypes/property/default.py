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

from lib.core.optypes.property.file.file_input_ui import property_fileinput_ui
from lib.core.optypes.property.file.file_output_ui import property_fileoutput_ui
from lib.core.optypes.property.file.save_bitmap_copy_ui import property_save_bitmap_copy_ui
from lib.core.optypes.property.file.image_info_ui import property_imageinfo_ui
from lib.core.optypes.property.file.undoredo_ui import property_undoredo_ui
from lib.core.optypes.property.file.cache_ui import property_cache_ui
from lib.core.optypes.property.file.view_ui import property_view_ui

from lib.core.optypes.property.edit.transform_image_ui import property_transformimage_ui
from lib.core.optypes.property.edit.image_mode_ui import property_imagemode_ui

from lib.core.optypes.property.create.new_image_ui import property_newimage_ui
from lib.core.optypes.property.create.noise_image_ui import property_noiseimage_ui


def types_default(self):
    """ Loads default property panels. """

    ## these are to be in proper stacking order!
    property_fileinput_ui(self)
    property_fileoutput_ui(self)
    property_save_bitmap_copy_ui(self)
    property_imageinfo_ui(self)
    property_undoredo_ui(self)
    property_cache_ui(self)
    property_view_ui(self)

    property_transformimage_ui(self)
    property_imagemode_ui(self)

    property_newimage_ui(self)
    property_noiseimage_ui(self)

