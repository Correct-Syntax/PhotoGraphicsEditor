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
from tkinter import ttk

#from flatbutton import FlatButton

class DropDownMenu(Label):
    """ Drop Down Menu widget.

    Parameters
    ----------
    widget:
      The name of the DropDown Button to connect this widget with
    options:
      List of options for the menu (as strings)
    commands:
      Commands for each of the specified options as a dict, with the key being the
      option specified in the 'options' parameter
      Example: ...options=['Print'], commands={'Print':print_out(self)}...
    width:
      Width of the menu
    chars:
      Number of characters in the longest of the options specified
      EDIT: it seems to be based on pixels, not characters!! - specify the number of px
    default:
      Which option will be selected by default - must be an integer or None
    flagtext:
      Title of the menu
      """
    def __init__(self, widget, options=[], commands={}, width=10, chars=80, default=None,
                 flagtext=None):

        ## define variables
        self.widget = widget
        self.options = options
        self.commands = commands
        self.width = width
        self.defaultselection = default
        self.maxchars = chars
        self.flagtext = flagtext

        ## we want the menubutton to stay the same width
        self.widget.configure(width=self.maxchars + 6)

        ## binding to show the menu
        self.widget.bind("<ButtonPress>", self.enter)
            
        self.id = None
        self.tw = None

    def enter(self, event=None):
        if self.widget.cget("state") == DISABLED:
            return
        self.schedule()
        self.widget.configure(bg='grey50', fg='grey90')

    def leave(self, event=None):
        self.unschedule()
        self.hidemenu()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(0, self.showmenu)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showmenu(self, event=None):
        x = y = 0
        try:
            x, y, cx, cy = self.widget.bbox("insert")
        except:
            pass
        
        x += self.widget.winfo_rootx()
        y += self.widget.winfo_rooty() + 22
        
        ## create a toplevel window
        self.tplvl = Toplevel(self.widget)
        self.tplvl.wm_overrideredirect(True)
        self.tplvl.wm_geometry("+%d+%d" % (x, y))
        
        ## Make the menu to have some transparency and color
        self.tplvl.attributes("-alpha", 0.9)
        self.tplvl.configure(bg='grey40')
    
        ## Listbox
        self.Menu_Listbox = Listbox(
            self.tplvl,
            bg='grey40',
            fg='white',
            font=("Calibri", 10),
            highlightbackground='grey40',
            highlightcolor='grey40',
            width=self.width + 2,
            height=5,
            relief=FLAT,
            activestyle='none',
            selectbackground='#94afc9',
            selectforeground='black'
            )
        self.Menu_Listbox.pack(side=TOP, fill=BOTH)

        if self.flagtext != None:
            ## Separator
            Separator = ttk.Separator(self.tplvl, orient=HORIZONTAL,
                                      style="Line.TSeparator")
            Separator.pack(padx=2, side=TOP, fill=X)
        
            ## MenuFlag
            self.MenuFlag_Label = Label(
                self.tplvl,
                bg='grey40',
                fg='grey70',
                font=("Arial", 8),
                text=self.flagtext,
                anchor=W
                )
            self.MenuFlag_Label.pack(side=TOP, fill=BOTH)

        ## Add the options to the listbox
        for option in self.options:
            self.Menu_Listbox.insert(END, option)

        ## Configure the height to be the number of lines
        self.Menu_Listbox.configure(height=self.Menu_Listbox.size())

        ## Set the default selection
        if self.defaultselection != None:
            self.Menu_Listbox.selection_set(self.defaultselection)

        ## Binding to get the option
        self.Menu_Listbox.bind("<Double-Button-1>", lambda event: self.hidemenu())

        ## Bindings to destroy the menu
        self.widget.bind("<Button-1>", lambda event: self.hidemenu())
        self.tplvl.bind("<Leave>", self.leave)
        

    def hidemenu(self):
        try:
            ## Get the current selection
            sel = self.Menu_Listbox.get(ACTIVE)

            ## configure the menubutton text
            self.widget.configure(text=sel)
            
            ## we want the menubutton to stay the same width
            self.widget.configure(width=self.maxchars + 6)
            
            ## get the command from the dict
            command = self.commands[sel]

            ## Run a command, if there was one specified
            if command != None:
                command()

            ## Destroy the menu
            self.tplvl.destroy()

            ## unbind binding
            self.widget.unbind("<Button-1>")

        except:
            ## Destroy the menu
            self.tplvl.destroy()

            ## unbind binding
            self.widget.unbind("<Button-1>")


## example code
if __name__ == '__main__':
    
    def add(c):
        print('add')
        print(c)
      
    from dropdownbutton import DropDownButton

    root = Tk()
    c = 'hello'
    Dropdown = DropDownButton(root, text='Add')
    Dropdown.grid(row=0, column=1, padx=1, pady=6)
    DropDownMenu(Dropdown,
                 options=[
                     'Add',
                     'Add Mod'
                     ],
                 commands={
                     'Add': lambda:add(c),
                     'Add Mod': lambda:add(c)
                     },
                 flagtext="Blend Mode")

    root.mainloop()

