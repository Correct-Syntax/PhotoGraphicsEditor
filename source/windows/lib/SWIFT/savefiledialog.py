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
## Adapted from the tkinter FileDialog, by Fredrik Lundh

import os
import fnmatch
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

from lib.SWIFT.flatbutton import FlatButton
from lib.SWIFT.tooltip import ToolTip

dialogstates = {}

class SaveFile_Dialog(object):
    """ The base class for the save file dialog. """
    def __init__(self, master, title=None, initialfile='untitled.png',
                 filetypes=['.png', '.jpg']):
        self.master = master
        self.directory = None
        self.initialfile = initialfile
        self.supportedfiletypes = filetypes

        ## Toplevel window
        self.FileDialogWindow = Toplevel(master)
        self.FileDialogWindow.title(title)
        self.FileDialogWindow.iconname(title)
        x = self.FileDialogWindow.winfo_screenwidth()-775
        y = self.FileDialogWindow.winfo_screenheight()-600
        self.FileDialogWindow.geometry("775x600+%d+%d" % (x/2, y/2))
        self.FileDialogWindow.configure(bg='grey40')
        self.FileDialogWindow.transient(self.master)
        self.FileDialogWindow.wm_iconbitmap('lib/datafiles/icons/program/Program_Icon.ico')
        self.FileDialogWindow.resizable(width=False, height=False)
        self.FileDialogWindow.deiconify()

        ## Sidebar frame
        self.sidebarframe = Frame(self.FileDialogWindow, bg='grey40')
        self.sidebarframe.pack(fill=Y, side=LEFT)
        
        ## System frame
        System_lblfrm = Frame(self.sidebarframe, relief=SOLID, bd=1, bg='grey40')
        System_lblfrm.pack(padx=4, pady=4, side=TOP)

        self.system  = Listbox(System_lblfrm, exportselection=0,
                             bg='grey40',
                             fg='black',
                             font=("Calibri", 9),
                             highlightbackground='grey40',
                             highlightcolor='grey40',
                             height=5,
                             width=20,
                             relief=FLAT,
                             activestyle='none',
                             selectbackground='#94afc9',
                             selectforeground='black'
                             )
        self.system.pack(padx=4, pady=4, side=TOP)

        self.system.insert(END, '(C:)')
        self.system.insert(END, '(D:)')
        self.system.insert(END, '(E:)')

        ## Check if any extra drives exist
        if os.path.exists('F:/') == True:
            self.system.insert(END, '(F:)')
            
        if os.path.exists('G:/') == True:
            self.system.insert(END, '(G:)')

        if os.path.exists('H:/') == True:
            self.system.insert(END, '(H:)')

        if os.path.exists('I:/') == True:
            self.system.insert(END, '(I:)')

        if os.path.exists('J:/') == True:
            self.system.insert(END, '(J:)')

        if os.path.exists('K:/') == True:
            self.system.insert(END, '(K:)')

        self.system.selection_set(0)
        self.system.bind('<Button-1>', self.on_system_select_event)

        ## Main frame
        self.mainframe = Frame(self.FileDialogWindow, relief=SOLID, bd=1, bg='grey40')
        self.mainframe.pack(padx=4, pady=4, side=LEFT, fill=BOTH)
        
        self.maintopframe = Frame(self.mainframe, bg='grey40')
        self.maintopframe.pack(side=TOP, fill=X)

        self.FileDialogWindowframe = Frame(self.maintopframe, bg='grey40')
        self.FileDialogWindowframe.pack(fill=X)

        self.filter = Entry(self.FileDialogWindowframe, selectbackground='#94afc9',
                            bg='grey70', fg='black', font=("Calibri", 11),
                            selectforeground='white', insertbackground='grey40')
        self.filter.pack(pady=2, padx=2, side=TOP, fill=X)
        self.filter.bind('<Return>', self.filter_command)

        self.selection = Entry(self.FileDialogWindowframe, selectbackground='#94afc9',
                               bg='grey70', fg='black', font=("Calibri", 11),
                               selectforeground='white', insertbackground='grey40')
        self.selection.pack(pady=2, padx=2, side=TOP, fill=X)
        self.selection.bind('<Return>', self.ok_event)

        self.buttonsframe = Frame(self.maintopframe, bg='grey40')
        self.buttonsframe.pack(side=RIGHT, fill=X)

        ## Buttons
        self.ok_button = FlatButton(self.buttonsframe,
                                 text=" Save File ",
                                 command=self.ok_command)
        self.ok_button.pack(padx=2, pady=2, side=LEFT)
        ToolTip(self.ok_button, "Save file as given filetype", wtype='FLATBUTTON')
        
        self.cancel_button = FlatButton(self.buttonsframe,
                                    text=" Cancel ",
                                    command=self.cancel_command)
        self.cancel_button.pack(padx=2, pady=2,  side=RIGHT)
        ToolTip(self.cancel_button, "Cancel and close dialog", wtype='FLATBUTTON')

        self.midframe = Frame(self.mainframe)
        self.midframe.pack(expand=YES, side=BOTTOM,fill=BOTH)

        self.filesbar = Scrollbar(self.midframe)
        self.filesbar.pack(side=RIGHT, fill=Y)
        self.files = Listbox(self.midframe, exportselection=0,
                             yscrollcommand=(self.filesbar, 'set'),
                             bg='grey40',
                             fg='white',
                             font=("Calibri", 10),
                             highlightbackground='grey60',
                             highlightcolor='grey60',
                             height=5,
                             width=40,
                             relief=FLAT,
                             activestyle='none',
                             selectbackground='#94afc9',
                             selectforeground='black'
                             )
        self.files.pack(side=RIGHT, expand=YES, fill=BOTH)
        btags = self.files.bindtags()
        self.files.bindtags(btags[1:] + btags[:1])
        self.files.bind('<ButtonRelease-1>', self.files_select_event)
        self.files.bind('<Double-ButtonRelease-1>', self.files_double_event)
        self.filesbar.config(command=(self.files, 'yview'))

        self.dirsbar = Scrollbar(self.midframe)
        self.dirsbar.pack(side=LEFT, fill=Y)
        self.dirs = Listbox(self.midframe, exportselection=0,
                            yscrollcommand=(self.dirsbar, 'set'),
                             bg='grey40',
                             fg='white',
                             font=("Calibri", 10),
                             highlightbackground='grey60',
                             highlightcolor='grey60',
                             height=5,
                             width=40,
                             relief=FLAT,
                             activestyle='none',
                             selectbackground='#94afc9',
                             selectforeground='black'
                            )
        self.dirs.pack(side=LEFT, expand=YES, fill=BOTH)
        self.dirsbar.config(command=(self.dirs, 'yview'))
        btags = self.dirs.bindtags()
        self.dirs.bindtags(btags[1:] + btags[:1])
        self.dirs.bind('<ButtonRelease-1>', self.dirs_select_event)
        self.dirs.bind('<Double-ButtonRelease-1>', self.dirs_double_event)
        self.FileDialogWindow.protocol('WM_DELETE_WINDOW', self.cancel_command)

        ## XXX Are the following okay for a general audience?
        self.FileDialogWindow.bind('<Alt-w>', self.cancel_command)
        self.FileDialogWindow.bind('<Alt-W>', self.cancel_command)

    def on_system_select_event(self, event):
        self.filter.delete(0 ,END)
        self.selection.delete(0 ,END)
        sel = self.system.get('active')

        ## Drives
        if sel == '(C:)':
            systemdir = 'C:/'

        if sel == '(D:)':
            systemdir = 'D:/'

        if sel == '(E:)':
            systemdir = 'E:/'

        if sel == '(F:)':
            systemdir = 'F:/'

        if sel == '(G:)':
            systemdir = 'G:/'

        if sel == '(H:)':
            systemdir = 'H:/'

        if sel == '(I:)':
            systemdir = 'I:/'

        if sel == '(J:)':
            systemdir = 'J:/'

        if sel == '(K:)':
            systemdir = 'K:/'

        ## If the drive was selected, insert into the listbox
        self.filter.insert(0, systemdir)
        self.dirs_double_event(None)

    def go(self, directory_or_file="C:/", pattern="*"):
        ## get the main directory, example: "C:/Users/"
        directory_or_file = os.path.expanduser(directory_or_file)

        ## if the path is a folder (dir)
        if os.path.isdir(directory_or_file):
            self.directory = directory_or_file
        ## if it is a file, split the path and assign the file as default
        else:
            self.directory, default = os.path.split(directory_or_file)
            
        self.set_filter(self.directory, pattern)
        self.set_selection(self.initialfile)
        self.filter_command()
        self.selection.focus_set()
        self.FileDialogWindow.wait_visibility()## window needs to be visible for the grab
        self.FileDialogWindow.grab_set()
        self.how = None
        self.master.mainloop()## Exited by self.quit(how)
        self.FileDialogWindow.destroy()
        return self.how

    def set_filter(self, dir, pat):
        ## if the path is NOT an absolute pathname, we need to make it absolute
        if not os.path.isabs(dir):
            try:
                pwd = os.getcwd()
            except OSError:
                pwd = None
            if pwd:
                dir = os.path.join(pwd, dir)
                dir = os.path.normpath(dir)

        ## clear the entry
        self.filter.delete(0, END)

        ## insert the path into the entry
        self.filter.insert(END, os.path.join(dir or os.curdir, pat or "*"))

    def set_selection(self, file):
        ## clear all the options in the entry
        self.selection.delete(0, END)
        
        ## insert the filename into the entry
        self.selection.insert(END, file)

    def filter_command(self, event=None):
        ## get the directory
        dir, pat = self.get_filter()

        ## try to get all the names of the files and folders in the directory
        try:
            names = os.listdir(dir)
        except OSError:
            self.master.bell()
            return

        ## set self.directory as the main directory
        self.directory = dir

        ## sort the filenames
        self.set_filter(dir, pat)
        names.sort()

        ## get the constant string used by the OS to refer to the parent directory
        subdirs = [os.pardir]

        ## iterate over the files
        matchingfiles = []
        for name in names:
            fullname = os.path.join(dir, name)
            ## make sure that it is a dir before appending to the list of filenames
            if os.path.isdir(fullname):
                subdirs.append(name)
            elif fnmatch.fnmatch(name, pat):
                matchingfiles.append(name)

        ## clear all the options in the listbox
        self.dirs.delete(0, END)

        ## update the subdir option
        for name in subdirs:
            self.dirs.insert(END, name)
        self.files.delete(0, END)

        ## only show files if they are in the list of supported filetypes
        for name in matchingfiles:
            ext = os.path.splitext(name)[1]
            if ext.lower() in self.supportedfiletypes:
                self.files.insert(END, name)
            head, tail = os.path.split(self.get_selection())
            if tail == os.curdir: tail = ''
            self.set_selection(tail)

    def get_filter(self):
        filter = self.filter.get()
        filter = os.path.expanduser(filter)
        if filter[-1:] == os.sep or os.path.isdir(filter):
            filter = os.path.join(filter, "*")
        return os.path.split(filter)

    def quit(self, how=None):
        self.how = how
        self.master.quit()## Exit the mainloop()

    def dirs_double_event(self, event):
        self.filter_command()

    def dirs_select_event(self, event):
        dir, pat = self.get_filter()
        print(dir, pat)
        subdir = self.dirs.get('active')
        dir = os.path.normpath(os.path.join(self.directory, subdir))
        self.set_filter(dir, pat)      

    def files_double_event(self, event):
        self.ok_command()

    def files_select_event(self, event):
        file = self.files.get('active')
        self.set_selection(file)

    def ok_event(self, event):
        self.ok_command()

    def ok_command(self):
        self.quit(self.get_selection())

    def get_selection(self):
        f = self.filter.get()
        length = len(f)
        path = f[0: length-1]
        file = os.path.join(path, self.selection.get())
        file = os.path.expanduser(file)
        return file
    
    def cancel_command(self, event=None):
        self.quit()


class SaveFileDialog(SaveFile_Dialog):
    """File selection dialog to save a file. """

    def ok_command(self):
        file = self.get_selection()
        if os.path.exists(file):
            if os.path.isdir(file):
                self.master.bell()
                return
            d = messagebox.askyesno("Overwrite Existing File?",
                       "Overwrite existing file {}?".format(file), icon='warning')
            if d != True:
                return
        else:
            head, tail = os.path.split(file)
            if not os.path.isdir(head):
                self.master.bell()
                return
        self.quit(file)
