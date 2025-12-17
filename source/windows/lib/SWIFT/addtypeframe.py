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
from PIL import ImageTk

from lib.SWIFT.tooltip import ToolTip


class AddTypeFrame(object):
   """ Add Modifier Frame widget.

    Parameters
    ----------

    """
   def __init__(self, master, options=[], commands={}, width=10, title='', tooltip=''):
      self.master = master
      self.options = options
      self.commands = commands
      self.width = width
      self.title = title
      self.tooltip = tooltip

      ## create the main frame
      self.AddType_Frame = Frame(self.master, background="#969696")
      self.AddType_Frame.pack(fill=X)

      ## Title
      Title_Label = Label(
         self.AddType_Frame,
         bg='#969696',
         fg='black',
         font=("Arial", 8),
         text=self.title,
         anchor=W
         )
      Title_Label.pack(side=TOP, fill=BOTH)

      ## icon
      self.IconSearch = ImageTk.PhotoImage(file="lib/SWIFT/bitmaps/Search.png")

      ## search frame
      self.SearchAddType_Frame = Frame(self.AddType_Frame, background="#969696")
      self.SearchAddType_Frame.pack(fill=X)
      
      ## Search label
      self.SearchAddType_Label = Label(self.SearchAddType_Frame, image=self.IconSearch,
                                       background="#969696")
      self.SearchAddType_Label.pack(padx=2, pady=2, side=LEFT)
         
      ## Search entry
      self.SearchAddType_Var = StringVar()
      self.SearchAddType_Var.trace('w', lambda name, index, mode: self._update_listbox())
      self.SearchAddType_Entry = Entry(
         self.SearchAddType_Frame,
         textvariable=self.SearchAddType_Var,
         selectbackground='#94afc9',
         bg='grey70',
         width=25,
         fg='black',
         font=("Calibri", 10),
         selectforeground='white',
         insertbackground='grey40'
         )
      self.SearchAddType_Entry.pack(padx=2, pady=2, side=LEFT, fill=X)
      ToolTip(self.SearchAddType_Entry, self.tooltip)

      ## frame
      AddTypeListbox_Frame = Frame(self.AddType_Frame, bg='#969696')
      AddTypeListbox_Frame.pack(padx=4, side=TOP, fill=X)

      ## scrollbar
      self.yScroll = Scrollbar(AddTypeListbox_Frame, orient=VERTICAL)
      self.yScroll.pack(padx=1, pady=1, side=RIGHT, fill=Y)

      ## listbox
      self.AddType_Listbox = Listbox(
         AddTypeListbox_Frame,
         bg='grey40',
         fg='white',
         font=("Calibri", 10),
         highlightbackground='grey40',
         highlightcolor='grey40',
         width=self.width + 2,
         height=4,
         relief=FLAT,
         activestyle='none',
         selectbackground='#94afc9',
         selectforeground='black',
         yscrollcommand=self.yScroll.set
         )
      self.AddType_Listbox.pack(padx=2, pady=2, side=LEFT)
      
      self.yScroll['command'] = self.AddType_Listbox.yview

      ## update the listbox according to the search 
      self._update_listbox()

      ## binding to get the option
      self.AddType_Listbox.bind("<Double-Button-1>", lambda event: self._get_value())


   def _update_listbox(self):
      ## setup to update list
      searched_var = self.SearchAddType_Var.get()
      self.AddType_Listbox.delete(0, END)

      ## add the options that match the search to the listbox
      for item in self.options:
         if searched_var.lower() in item.lower():
             self.AddType_Listbox.insert(END, item)
                

   def _get_value(self, event=None):
      ## Get the current selection
      sel = self.AddType_Listbox.get(ACTIVE)

      ## get the command from the dict
      command = self.commands[sel]

      ## Run a command, if there was one specified
      if command != None:
          command()
