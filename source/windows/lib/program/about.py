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
from PIL import ImageTk

from lib.SWIFT.tooltip import ToolTip
from lib.SWIFT.flatbutton import FlatButton
from lib.SWIFT.tabbednotebook import Notebook


def about_program(self):
    AboutWindow = Toplevel(self)
    AboutWindow.title('About PhotoGraphics Editor')
    AboutWindow.wm_iconbitmap('lib/datafiles/icons/program/Program_Icon.ico')
    AboutWindow.geometry('450x590')
    AboutWindow.transient(self)
    AboutWindow.update_idletasks()
    AboutWindow.deiconify()
    AboutWindow.configure(bg="#969696")


    AboutWindow_Tabs = Notebook(AboutWindow)

    About_Tab = Frame(AboutWindow_Tabs(), bg="#969696")
    Libraries_Tab = Frame(AboutWindow_Tabs(), bg="#969696")
    Changelog_Tab = Frame(AboutWindow_Tabs(), bg="#969696")
    License_Tab = Frame(AboutWindow_Tabs(), bg="#969696")

###########
## About ##
###########

    ## Logo
    Logo_Canvas = Canvas(About_Tab, width=200, height=200, highlightthickness=0,
                         bg="#969696")
    Logo_Canvas.pack(side=TOP)

    self.ICON = PhotoImage(file='lib/datafiles/icons/program/Program_Logo.png') 
    Logo_Canvas.create_image(0, 0, image=self.ICON, anchor=NW)
    
    ## Labels 
    About_Tab_lbl1 = Label(About_Tab, text='PhotoGraphics Editor 1.1.0', bg="#969696",
                           font=("Georgia", 15))
    About_Tab_lbl1.pack(padx=4, pady=4)
    
    About_Tab_lbl2 = Label(About_Tab, text='''Copyright (C) 2019 Noah Rahm
    _____________________________________

    PhotoGraphics Editor is a free and open source image editing program
    written in the Python Programming Language

    All glory and praise to Yahweh!''', bg="#969696", font=("Arial", 8))
    About_Tab_lbl2.pack(padx=4, pady=4, side=TOP)


###############
## Libraries ##
###############

    ## Labels 
    Libraries_Tab_lbl1 = Label(Libraries_Tab, text='Third-Party Libraries',
                               bg="#969696", font=("Arial Bold", 12))
    Libraries_Tab_lbl1.pack(padx=4, pady=4)

    Libraries_Tab_lbl2 = Label(Libraries_Tab, text='''
    Python 3.4.3

    tkinter (Tk 8.6.1)

    ttk 0.3.2

    PIL 4.0.0

    Scipy 0.15.0

    Numpy 1.8.1
    ''', bg="#969696", font=("Arial", 10))
    Libraries_Tab_lbl2.pack(padx=4, pady=4)

###############
## Changelog ##
###############

    ## Label 
    Changelog_Tab_lbl1 = Label(Changelog_Tab, text='Changelog', bg="#969696",
                               font=("Arial Bold", 12))
    Changelog_Tab_lbl1.pack(padx=4, pady=4)

    ## Frame
    Changelog_Tab_LogFrame = Frame(Changelog_Tab, bg="#969696")
    Changelog_Tab_LogFrame.pack(padx=4, pady=4)

    ## Log
    Changelog_Tab_Log = Text(Changelog_Tab_LogFrame, relief=GROOVE, wrap=WORD,
                             highlightthickness=0, bd=2, font=("Arial", 10))
    Changelog_Tab_LogScrollBar = Scrollbar(Changelog_Tab_LogFrame, orient=VERTICAL,
                                           command=Changelog_Tab_Log.yview)
    Changelog_Tab_LogScrollBar.pack(side=RIGHT, fill=Y)
    Changelog_Tab_Log.configure(yscrollcommand=Changelog_Tab_LogScrollBar.set)
    Changelog_Tab_Log.pack(padx=4, pady=4)

    ## Insert text into Log
    CHANGELOG_TEXT = open('lib/datafiles/files/changelog.txt', 'r')
    Changelog_Tab_Log.insert(INSERT, CHANGELOG_TEXT.read())

    ## Disable the widget so that it cannot be edited
    Changelog_Tab_Log.configure(state=DISABLED)

#############
## License ##
#############

    ## Labels
    License_Tab_lbl1 = Label(License_Tab, text='License', bg="#969696",
                             font=("Arial Bold", 12))
    License_Tab_lbl1.pack(padx=4, pady=4)
    
    License_Text = open('lib/datafiles/files/license.txt', 'r').read()

    License_Label = Label(License_Tab, text=License_Text, bg="#969696",
                          font=("Arial", 8))
    License_Label.pack(padx=4, pady=4)

###############
## OK Button ##
###############
    OK_btn = FlatButton(AboutWindow, text='    OK    ', command=AboutWindow.destroy)
    OK_btn.pack(padx=2, pady=4, side=BOTTOM)
    ToolTip(OK_btn, "Close about window", wtype='FLATBUTTON')
    

    ## add the tabs
    AboutWindow_Tabs.add_tab(About_Tab, title=' About  ')
    AboutWindow_Tabs.add_tab(Libraries_Tab, title=' Libraries  ')
    AboutWindow_Tabs.add_tab(Changelog_Tab, title=' Changelog  ')
    AboutWindow_Tabs.add_tab(License_Tab, title=' License  ')
