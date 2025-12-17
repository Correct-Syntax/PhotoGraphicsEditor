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
import subprocess
from tkinter import messagebox


def program_documentation(self):
    try:
        ## Open the HTML docs in the default web browser
        subprocess.Popen(['start', str(os.getcwd() + "\lib\docs\index.html")], shell=True)
    except:
        messagebox.showerror(title="Error!", message='''
        The program encountered an error while attempting to find the documentation

        This could be caused by one or more of the following situations:
        - You do not have a web browser associated with .html files
        - The documentation was deleted, corrupted or moved from the expected location
        ''')
