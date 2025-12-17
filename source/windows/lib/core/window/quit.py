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
from tkinter import messagebox


def quit_program(self):
    """ Quits the program. """
    ## Find out if the user really wants to quit the program
    a = messagebox.askyesno('Quit?','''
Any unsaved data will be lost!

Are you sure you would like to quit?
''', icon='warning')

    # if so, destroy the window
    if a == True:
        self.destroy()
    else:
        pass
