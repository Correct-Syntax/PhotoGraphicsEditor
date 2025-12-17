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
from tkinter import ttk

from lib.SWIFT.tooltip import ToolTip
from lib.program.about import about_program
from lib.program.documentation import program_documentation


def topbar_ui(self):
    self.Topbar_Frame = Frame(self, bd=1, relief=RIDGE, bg="#7e7e7e")
    self.Topbar_Frame.pack(padx=0, pady=0, fill=X, side=TOP)

    AboutProgram_Label = Label(self.Topbar_Frame, image=self.ABOUTPROGRAM_ICON,
                               bd=0.5, relief=SOLID, background="#969696")
    AboutProgram_Label.pack(padx=4, pady=2, ipadx=2, ipady=2, side=LEFT)
    ToolTip(AboutProgram_Label, "About PhotoGraphics Editor")
    AboutProgram_Label.bind("<Button-1>", lambda event: about_program(self))
    
    Documentation_Label = Label(self.Topbar_Frame, image=self.DOCUMENTATION_ICON,
                                bd=0.5, relief=SOLID, background="#969696")
    Documentation_Label.pack(padx=4, pady=2, ipadx=2, ipady=2, side=LEFT)
    ToolTip(Documentation_Label, "PhotoGraphics Editor Documentation")
    Documentation_Label.bind("<Button-1>", lambda event: program_documentation(self))

    UserPreferences_Label = Label(self.Topbar_Frame, image=self.USERPREFERENCES_ICON,
                                  bd=0.5, relief=SOLID, background="#969696")
    UserPreferences_Label.pack(padx=4, pady=2, ipadx=2, ipady=2, side=LEFT)
    ToolTip(UserPreferences_Label, "User Preferences")
    #UserPreferences_Label.bind("<Button-1>", (self))

    ProgramName_Label = Label(self.Topbar_Frame, text=' PhotoGraphics Editor v1.1.0 ', background="#7e7e7e")
    ProgramName_Label.pack(padx=4, pady=2, side=LEFT)
    
    Icon_Label = Label(self.Topbar_Frame, image=self.MAINPROGRAM_ICON, background="#7e7e7e")
    Icon_Label.pack(padx=4, pady=2, side=LEFT)

    self.TopbarInfo_Label = Label(self.Topbar_Frame, text='', bg="#7e7e7e")
    self.TopbarInfo_Label.pack(padx=4, pady=2, side=LEFT)
